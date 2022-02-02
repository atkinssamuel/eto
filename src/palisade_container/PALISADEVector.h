//
// Created by atkinswsl on 1/16/22.
//

#ifndef ETO_PALISADEVECTOR_H
#define ETO_PALISADEVECTOR_H
#include "utils.h"

using namespace lbcrypto;

class PALISADEVector {
public:
    shared_ptr<CiphertextImpl<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>>>
    ciphertext;
    int _size;
    int _unpadded_size;
    int size();
    int unpadded_size();
    PALISADEVector();
    PALISADEVector(
        shared_ptr<CiphertextImpl<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>>>
        ct, int s);
};

int PALISADEVector::size() {
    return _size;
}

int PALISADEVector::unpadded_size() {
    return _unpadded_size;
}

PALISADEVector::PALISADEVector(
    shared_ptr<CiphertextImpl<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>>>
    ct, int unpadded_size) {
    _unpadded_size = unpadded_size;
    _size = next_2_power(unpadded_size);
    ciphertext = std::move(ct);
}


#endif //ETO_PALISADEVECTOR_H
