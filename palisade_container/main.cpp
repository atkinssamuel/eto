//
// Created by atkinswsl on 12/22/21.
//

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include "palisade.h"

namespace py = pybind11;
using namespace lbcrypto;

CryptoContext<DCRTPoly> GenerateCryptoContext(RescalingTechnique rsTech, uint32_t multDepth, uint32_t scaleFactorBits, uint32_t batchSize, SecurityLevel securityLevel, uint32_t ringDimension){
    return CryptoContextFactory<DCRTPoly>::genCryptoContextCKKS(multDepth, scaleFactorBits, batchSize, securityLevel, ringDimension,
                                                                rsTech);
}

LPKeyPair<Element> generate_keys(CryptoContext<DCRTPoly> cc){
    return cc->KeyGen();
}

class PALISADE{
    RescalingTechnique rsTech = EXACTRESCALE;
    uint32_t multDepth = 5;
    uint32_t scaleFactorBits = 50;
    uint32_t batchSize = 8;
    SecurityLevel securityLevel = HEStd_128_classic;
    uint32_t ringDimension = 0;
    CryptoContext<DCRTPoly> cc = GenerateCryptoContext(rsTech, multDepth, scaleFactorBits, batchSize, securityLevel, ringDimension);
    auto keys
public:
    PALISADE();
};

PALISADE::PALISADE(){
    cc =
    cc->Enable(ENCRYPTION);
    cc->Enable(SHE);
    cc->Enable(LEVELEDSHE);

    auto keys = cc->KeyGen();
    cc->EvalMultKeyGen(keys.secretKey);
}


void palisade_example(){
    PALISADE palisade = PALISADE();

}



// C++ in Python the Easy Way! #pybind11 https://www.youtube.com/watch?v=_5T70cAXDJ0
PYBIND11_MODULE(PALISADE, handle){
    handle.def("palisade_example", &palisade_example);

    handle.doc() = "pybind11";
}
