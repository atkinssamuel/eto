//
// Created by atkinswsl on 12/22/21.
//

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

#include <utility>
#include "palisade.h"

namespace py = pybind11;
using namespace lbcrypto;

vector<double> splice_vector(vector<double> x, int start, int end){
    if (start < 0){
        throw std::invalid_argument("Received a start value less than 0.");
    }
    if (end >= int(x.size())){
        throw invalid_argument("Received an end value greater than the size of the input vector");
    }
    auto first = x.cbegin() + start;
    auto last = x.cbegin() + end;

    vector<double> vec(first, last);
    return vec;
}

CryptoContext<DCRTPoly> GenerateCryptoContext(RescalingTechnique rsTech, uint32_t multDepth, uint32_t scaleFactorBits, uint32_t batchSize, SecurityLevel securityLevel, uint32_t ringDimension){
    CryptoContext<DCRTPoly> cc = CryptoContextFactory<DCRTPoly>::genCryptoContextCKKS(multDepth, scaleFactorBits, batchSize, securityLevel, ringDimension,
                                                                rsTech);
    cc->Enable(ENCRYPTION);
    cc->Enable(SHE);
    cc->Enable(LEVELEDSHE);
    return cc;
}

LPKeyPair<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>> GenerateKeys(const CryptoContext<DCRTPoly>& cc){
    auto keys = cc->KeyGen();
    cc->EvalMultKeyGen(keys.secretKey);
    cc->EvalSumKeyGen(keys.secretKey);
    return keys;
}

class PALISADEVector{
public:
    shared_ptr<CiphertextImpl<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>>> ciphertext;
    int size;
    explicit PALISADEVector(shared_ptr<CiphertextImpl<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>>> ct, int s);
};

PALISADEVector::PALISADEVector(
        shared_ptr<CiphertextImpl<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>>> ct, int s) {
    size = s;
    ciphertext = std::move(ct);
}

class PALISADE {
    RescalingTechnique rsTech = EXACTRESCALE;
    uint32_t multDepth = 5;
    uint32_t scaleFactorBits = 50;
    SecurityLevel securityLevel = HEStd_128_classic;
    uint32_t ringDimension = 0;
public:
    uint32_t batchSize = 8;
    CryptoContext<DCRTPoly> cc = GenerateCryptoContext(rsTech, multDepth, scaleFactorBits, batchSize, securityLevel,
                                                       ringDimension);
    LPKeyPair<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>> keys = GenerateKeys(cc);

    PALISADEVector encrypt_vector(const vector<double> &vector);
    vector<double> decrypt_vector(const PALISADEVector &pv);
    PALISADEVector hadamard(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector dot(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector add(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector sum(const PALISADEVector &pv);
    PALISADEVector op(const PALISADEVector &pv1, const PALISADEVector &pv2);
};

PALISADEVector PALISADE::op(const PALISADEVector& pv1, const PALISADEVector& pv2){
    return pv1;
}

PALISADEVector PALISADE::encrypt_vector(const vector<double>& vector){
    return PALISADEVector(cc->Encrypt(keys.publicKey, cc->MakeCKKSPackedPlaintext(vector)), int(vector.size()));
}

vector<double> PALISADE::decrypt_vector(const PALISADEVector& pv){
    Plaintext result;
    cc->Decrypt(keys.secretKey, pv.ciphertext, &result);
    vector<double> x = result->GetRealPackedValue();
    return splice_vector(x, 0, pv.size);
}

PALISADEVector PALISADE::hadamard(const PALISADEVector& pv1, const PALISADEVector& pv2){
    return PALISADEVector(cc->EvalMult(pv1.ciphertext, pv2.ciphertext), pv1.size);
}

PALISADEVector PALISADE::dot(const PALISADEVector& pv1, const PALISADEVector& pv2){
    return PALISADEVector(cc->EvalInnerProduct(pv1.ciphertext, pv2.ciphertext, pv1.size), 1);
}

PALISADEVector PALISADE::add(const PALISADEVector& pv1, const PALISADEVector& pv2){
    return PALISADEVector(cc->EvalAdd(pv1.ciphertext, pv2.ciphertext), pv1.size);
}

PALISADEVector PALISADE::sum(const PALISADEVector &pv){
    return PALISADEVector(cc->EvalSum(pv.ciphertext, pv.size), 1);
}


void palisade_example(){
    PALISADE palisade = PALISADE();

    vector<double> x = {2.0, 3.0};
    Plaintext ptxt = palisade.cc->MakeCKKSPackedPlaintext(x);

    shared_ptr<CiphertextImpl<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>>> c = palisade.cc->Encrypt(palisade.keys.publicKey, ptxt);
    auto c2 = palisade.cc->EvalInnerProduct(c, c, 8);

    Plaintext result;
    std::cout.precision(8);
    palisade.cc->Decrypt(palisade.keys.secretKey, c2, &result);
    result->SetLength(palisade.batchSize);
    std::cout << result << std::endl;


    std::cout << palisade.decrypt_vector(palisade.encrypt_vector(x)) << std::endl;

}



// C++ in Python the Easy Way! #pybind11 https://www.youtube.com/watch?v=_5T70cAXDJ0
PYBIND11_MODULE(PALISADEContainer, handle){
    py::class_<PALISADE>(handle, "PALISADE")
            .def(py::init())
            .def("encrypt_vector", &PALISADE::encrypt_vector)
            .def("decrypt_vector", &PALISADE::decrypt_vector)
            .def("hadamard", &PALISADE::hadamard)
            .def("dot", &PALISADE::dot)
            .def("add", &PALISADE::add)
            .def("sum", &PALISADE::sum);
    
    py::class_<PALISADEVector>(handle, "PALISADEVector"); // NOLINT(bugprone-unused-raii)


    handle.def("palisade_example", &palisade_example);

    handle.doc() = "pybind11";
}
