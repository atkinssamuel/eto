//
// Created by atkinswsl on 1/16/22.
//

#ifndef ETO_PALISADE_H
#define ETO_PALISADE_H

#include "palisade.h"
#include "PALISADEVector.h"

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
    uint32_t embedding_size;
    uint32_t M;
    CryptoContext<DCRTPoly> cc;
    LPKeyPair<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>> keys;

    PALISADEVector encrypt_vector(vector<double> &vector, bool wrapped);
    vector<double> decrypt_vector(const PALISADEVector &pv, int decimal_places);

    // Vector-Vector Operations:
    PALISADEVector v_hadamard(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector v_dot(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector v_add(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector v_sum(const PALISADEVector &pv);
    void set_rotation_vector_indices(const PALISADEVector &pv, vector<int> index_list);
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
    embedding_size = N/2;
    M = 2 * N;
}

PALISADEVector PALISADE::encrypt_vector(vector<double>& vector, bool wrapped){
    int unpadded_size = vector.size();
    int padded_size = next_2_power(unpadded_size);
    if (wrapped) {
        // padding initial vector entry with zeros
        for (int i = unpadded_size; i < padded_size; i++){
            vector.push_back(0);
        }

        // duplicating initial "padded_size" vector throughout the rest of the vector
        int orig_vect_ind = 0;
        for (int i = padded_size; i < int(embedding_size); i++){
            vector.push_back(vector[orig_vect_ind]);
            orig_vect_ind++;
        }
    }
    return PALISADEVector(cc->Encrypt(keys.publicKey, cc->MakeCKKSPackedPlaintext(vector)), unpadded_size);
}

vector<double> PALISADE::decrypt_vector(const PALISADEVector& pv, int decimal_places){
    Plaintext result;
    cc->Decrypt(keys.secretKey, pv.ciphertext, &result);
    vector<double> x = result->GetRealPackedValue();
    result->SetLength(batchSize);
    vector<double> spliced_vector = splice_vector(x, 0, pv._size);

    if (decimal_places != -1){
        for (int i = 0; i < int(spliced_vector.size()); i++){
            spliced_vector[i] = round_double(spliced_vector[i], decimal_places);
        }
    }
    return spliced_vector;
}


// Vector-Vector Operations:
PALISADEVector PALISADE::v_hadamard(const PALISADEVector& pv1, const PALISADEVector& pv2){
    return PALISADEVector(cc->EvalMult(pv1.ciphertext, pv2.ciphertext), pv1._size);
}

PALISADEVector PALISADE::v_dot(const PALISADEVector& pv1, const PALISADEVector& pv2){
    return PALISADEVector(cc->EvalInnerProduct(pv1.ciphertext, pv2.ciphertext, pv1._size), 1);
}

PALISADEVector PALISADE::v_add(const PALISADEVector& pv1, const PALISADEVector& pv2){
    return PALISADEVector(cc->EvalAdd(pv1.ciphertext, pv2.ciphertext), pv1._size);
}

PALISADEVector PALISADE::v_sum(const PALISADEVector &pv){
    auto cprecomp =   cc->EvalFastRotationPrecompute(pv.ciphertext);
    return PALISADEVector(cc->EvalSum(pv.ciphertext, pv._size), 1);
}
void PALISADE::set_rotation_vector_indices(const PALISADEVector &pv, vector<int> index_list){
    cc->EvalAtIndexKeyGen(keys.secretKey, index_list);
    cPrecomp = cc->EvalFastRotationPrecompute(pv.ciphertext);
}

PALISADEVector PALISADE::v_rot(const PALISADEVector &pv, int rot){
    return PALISADEVector(cc->EvalFastRotation(pv.ciphertext, rot, M, cPrecomp), pv._size);
}

// Vector-Constant Operations:
PALISADEVector PALISADE::vc_dot(const PALISADEVector& pv, const vector<double> cv){
    return PALISADEVector(cc->EvalInnerProduct(pv.ciphertext, cc->MakeCKKSPackedPlaintext(cv), pv._size), 1);
}

#endif //ETO_PALISADE_H
