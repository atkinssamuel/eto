//
// Created by atkinswsl on 1/16/22.
//

#ifndef ETO_PALISADE_H
#define ETO_PALISADE_H


#include "PALISADEVector.h"
#include "utils.h"

using namespace lbcrypto;

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
    PALISADEVector vector_hadamard(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector vector_dot(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector vector_add(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector vector_sum(const PALISADEVector &pv);

//    PALISADERowMatrix encrypt_row_matrix(const vector<vector<double>> &matrix);
//    vector<vector<double>> decrypt_row_matrix(const PALISADERowMatrix &prm);
};

PALISADEVector PALISADE::encrypt_vector(const vector<double>& vector){
    return PALISADEVector(cc->Encrypt(keys.publicKey, cc->MakeCKKSPackedPlaintext(vector)), int(vector.size()));
}

vector<double> PALISADE::decrypt_vector(const PALISADEVector& pv){
    Plaintext result;
    cc->Decrypt(keys.secretKey, pv.ciphertext, &result);
    vector<double> x = result->GetRealPackedValue();
    return splice_vector(x, 0, pv.size);
}

PALISADEVector PALISADE::vector_hadamard(const PALISADEVector& pv1, const PALISADEVector& pv2){
    return PALISADEVector(cc->EvalMult(pv1.ciphertext, pv2.ciphertext), pv1.size);
}

PALISADEVector PALISADE::vector_dot(const PALISADEVector& pv1, const PALISADEVector& pv2){
    return PALISADEVector(cc->EvalInnerProduct(pv1.ciphertext, pv2.ciphertext, pv1.size), 1);
}

PALISADEVector PALISADE::vector_add(const PALISADEVector& pv1, const PALISADEVector& pv2){
    return PALISADEVector(cc->EvalAdd(pv1.ciphertext, pv2.ciphertext), pv1.size);
}

PALISADEVector PALISADE::vector_sum(const PALISADEVector &pv){
    return PALISADEVector(cc->EvalSum(pv.ciphertext, pv.size), 1);
}

#endif //ETO_PALISADE_H
