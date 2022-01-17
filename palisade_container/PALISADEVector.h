//
// Created by atkinswsl on 1/16/22.
//

#ifndef ETO_PALISADEVECTOR_H
#define ETO_PALISADEVECTOR_H

using namespace lbcrypto;

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


#endif //ETO_PALISADEVECTOR_H
