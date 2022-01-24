//
// Created by atkinswsl on 1/16/22.
//

#ifndef ETO_PALISADE_H
#define ETO_PALISADE_H

#include "palisade.h"
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
    PALISADE(uint32_t bSize);
    uint32_t batchSize;
    shared_ptr<vector<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>>> cPrecomp;
    uint32_t N;
    uint32_t M;
    CryptoContext<DCRTPoly> cc;
    LPKeyPair<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>> keys;

    PALISADEVector encrypt_vector(const vector<double> &vector);
    vector<double> decrypt_vector(const PALISADEVector &pv);

    // Vector-Vector Operations:
    PALISADEVector v_hadamard(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector v_dot(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector v_add(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector v_sum(const PALISADEVector &pv);
    void set_rotation_vector(const PALISADEVector &pv);
    PALISADEVector v_rot(const PALISADEVector &pv, int rot);

    // Vector-Constant Operations:
    PALISADEVector vc_dot(const PALISADEVector &pv, vector<double> cv);
//    PALISADERowMatrix encrypt_row_matrix(const vector<vector<double>> &matrix);
//    vector<vector<double>> decrypt_row_matrix(const PALISADERowMatrix &prm);
};

PALISADE::PALISADE(uint32_t bSize){
    batchSize = bSize;
    cc = GenerateCryptoContext(rsTech, multDepth, scaleFactorBits, batchSize, securityLevel, ringDimension);
    keys = GenerateKeys(cc);
    N = cc->GetRingDimension();
    M = 2 * N;
}

PALISADEVector PALISADE::encrypt_vector(const vector<double>& vector){
    return PALISADEVector(cc->Encrypt(keys.publicKey, cc->MakeCKKSPackedPlaintext(vector)), int(vector.size()));
}

vector<double> PALISADE::decrypt_vector(const PALISADEVector& pv){
    Plaintext result;
    cc->Decrypt(keys.secretKey, pv.ciphertext, &result);
    vector<double> x = result->GetRealPackedValue();
    result->SetLength(batchSize);
    return splice_vector(x, 0, pv.size);
}


// Vector-Vector Operations:
PALISADEVector PALISADE::v_hadamard(const PALISADEVector& pv1, const PALISADEVector& pv2){
    return PALISADEVector(cc->EvalMult(pv1.ciphertext, pv2.ciphertext), pv1.size);
}

PALISADEVector PALISADE::v_dot(const PALISADEVector& pv1, const PALISADEVector& pv2){
    return PALISADEVector(cc->EvalInnerProduct(pv1.ciphertext, pv2.ciphertext, pv1.size), 1);
}

PALISADEVector PALISADE::v_add(const PALISADEVector& pv1, const PALISADEVector& pv2){
    return PALISADEVector(cc->EvalAdd(pv1.ciphertext, pv2.ciphertext), pv1.size);
}

PALISADEVector PALISADE::v_sum(const PALISADEVector &pv){
    auto cprecomp =   cc->EvalFastRotationPrecompute(pv.ciphertext);
    return PALISADEVector(cc->EvalSum(pv.ciphertext, pv.size), 1);
}

void PALISADE::set_rotation_vector(const PALISADEVector &pv){
    vector<int> index_list;
    for (int i = 1; i < 8192; i++){
        index_list.push_back(i);
    }
    cc->EvalAtIndexKeyGen(keys.secretKey, index_list);
    cPrecomp = cc->EvalFastRotationPrecompute(pv.ciphertext);
}

PALISADEVector PALISADE::v_rot(const PALISADEVector &pv, int rot){
    return PALISADEVector(cc->EvalFastRotation(pv.ciphertext, rot, M, cPrecomp), pv.size);
}

// Vector-Constant Operations:
PALISADEVector PALISADE::vc_dot(const PALISADEVector& pv, const vector<double> cv){
    return PALISADEVector(cc->EvalInnerProduct(pv.ciphertext, cc->MakeCKKSPackedPlaintext(cv), pv.size), 1);
}

#endif //ETO_PALISADE_H
