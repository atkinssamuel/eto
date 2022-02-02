//
// Created by atkinswsl on 1/16/22.
//

#ifndef ETO_PALISADE_H
#define ETO_PALISADE_H

#include "palisade.h"
#include "PALISADEMatrix.h"

using namespace lbcrypto;

CryptoContext<DCRTPoly> GenerateCryptoContext(RescalingTechnique rsTech,
        uint32_t multDepth,
        uint32_t scaleFactorBits, uint32_t batchSize, SecurityLevel securityLevel,
        uint32_t ringDimension) {
    CryptoContext<DCRTPoly> cc =
        CryptoContextFactory<DCRTPoly>::genCryptoContextCKKS(multDepth,
                scaleFactorBits, batchSize, securityLevel, ringDimension, rsTech);
    cc->Enable(ENCRYPTION);
    cc->Enable(SHE);
    cc->Enable(LEVELEDSHE);
    return cc;
}

LPKeyPair<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>> GenerateKeys(
    const CryptoContext<DCRTPoly>& cc) {
    auto keys = cc->KeyGen();
    cc->EvalMultKeyGen(keys.secretKey);
    cc->EvalSumKeyGen(keys.secretKey);
    return keys;
}

class PALISADE {
    RescalingTechnique rsTech = EXACTRESCALE;
    SecurityLevel securityLevel = HEStd_128_classic;
    uint32_t _ringDimension = 0;
    uint32_t _embedding_size;
    uint32_t _M;
    uint32_t _batchSize;
    uint32_t _scaleFactorBits;
    uint32_t _multDepth;
public:
    PALISADE(uint32_t mult_depth, uint32_t scaleFactorBits, uint32_t bSize);
    shared_ptr<vector<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>>> cPrecomp;
    CryptoContext<DCRTPoly> cc;
    LPKeyPair<DCRTPolyImpl<bigintfxd::BigVectorImpl<BigInteger>>> keys;

    // Property Definitions:
    int embedding_size();

    // Matrix Encryption:
//    PALISADEMatrix encrypt_matrix(vector<vector<double>> matrix, bool row_wise);

    // Vector Encryption:
    PALISADEVector encrypt_vector(vector<double> &vector, bool wrapped);
    vector<double> decrypt_vector(const PALISADEVector &pv, int decimal_places);

    // Vector-Vector Operations:
    PALISADEVector v_hadamard(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector v_dot(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector v_add(const PALISADEVector &pv1, const PALISADEVector &pv2);
    PALISADEVector v_sum(const PALISADEVector &pv);
    void set_rotation_indices(const PALISADEVector &pv,
                              vector<int> index_list);
    PALISADEVector v_rot(const PALISADEVector &pv, int rot);

    // Vector-Constant Operations:
    PALISADEVector vc_dot(const PALISADEVector &pv, const vector<double> &cv);
    PALISADEVector vc_hadamard(const PALISADEVector &pv, const vector<double> &cv);

    // Constant-Matrix Vector Operations:
    PALISADEVector cmv_mult(vector<vector<double>> cm, PALISADEVector pv);

//    PALISADERowMatrix encrypt_row_matrix(const vector<vector<double>> &matrix);
//    vector<vector<double>> decrypt_row_matrix(const PALISADERowMatrix &prm);
};

PALISADE::PALISADE(uint32_t mult_depth, uint32_t scaleFactorBits,
                   uint32_t bSize) {
    _multDepth = mult_depth;
    _scaleFactorBits = scaleFactorBits;
    _batchSize = bSize;
    cc = GenerateCryptoContext(rsTech, _multDepth, _scaleFactorBits, _batchSize,
                               securityLevel,
                               _ringDimension);
    keys = GenerateKeys(cc);
    _ringDimension = cc->GetRingDimension(); // N
    _embedding_size = _ringDimension / 2;
    _M = 2 * _ringDimension; // 2 * N
}

int PALISADE::embedding_size() {
    return int(_embedding_size);
}


PALISADEVector PALISADE::encrypt_vector(vector<double>& vector, bool wrapped) {
    int unpadded_size = vector.size();
    int padded_size = next_2_power(unpadded_size);
    if (wrapped) {
        // padding initial vector entry with zeros
        for (int i = unpadded_size; i < padded_size; i++)
            vector.push_back(0);

        // duplicating initial "padded_size" vector throughout the rest of the vector
        int orig_vect_ind = 0;
        for (int i = padded_size; i < int(_embedding_size); i++) {
            vector.push_back(vector[orig_vect_ind]);
            orig_vect_ind++;
        }
    }
    return PALISADEVector(cc->Encrypt(keys.publicKey,
                                      cc->MakeCKKSPackedPlaintext(vector)), unpadded_size);
}

vector<double> PALISADE::decrypt_vector(const PALISADEVector& pv,
                                        int decimal_places) {
    Plaintext result;
    cc->Decrypt(keys.secretKey, pv.ciphertext, &result);
    vector<double> x = result->GetRealPackedValue();
    result->SetLength(_batchSize);
    vector<double> spliced_vector = splice_vector(x, 0, pv._size);

    if (decimal_places != -1) {
        for (int i = 0; i < int(spliced_vector.size()); i++)
            spliced_vector[i] = round_double(spliced_vector[i], decimal_places);
    }
    return spliced_vector;
}


// Vector-Vector Operations:
PALISADEVector PALISADE::v_hadamard(const PALISADEVector& pv1,
                                    const PALISADEVector& pv2) {
    return PALISADEVector(cc->EvalMult(pv1.ciphertext, pv2.ciphertext), pv1._size);
}

PALISADEVector PALISADE::v_dot(const PALISADEVector& pv1,
                               const PALISADEVector& pv2) {
    return PALISADEVector(cc->EvalInnerProduct(pv1.ciphertext, pv2.ciphertext,
                          pv1._size), 1);
}

PALISADEVector PALISADE::v_add(const PALISADEVector& pv1,
                               const PALISADEVector& pv2) {
    return PALISADEVector(cc->EvalAdd(pv1.ciphertext, pv2.ciphertext),pv1._size);
}

PALISADEVector PALISADE::v_sum(const PALISADEVector &pv) {
    auto cprecomp =   cc->EvalFastRotationPrecompute(pv.ciphertext);
    return PALISADEVector(cc->EvalSum(pv.ciphertext, pv._size), 1);
}

void PALISADE::set_rotation_indices(const PALISADEVector &pv,
                                    vector<int> index_list) {
    cc->EvalAtIndexKeyGen(keys.secretKey, index_list);
    cPrecomp = cc->EvalFastRotationPrecompute(pv.ciphertext);
}

PALISADEVector PALISADE::v_rot(const PALISADEVector &pv, int rot) {
    return PALISADEVector(cc->EvalFastRotation(pv.ciphertext, rot, _M, cPrecomp),
                          pv._size);
}

// Vector-Constant Operations:
PALISADEVector PALISADE::vc_dot(const PALISADEVector &pv,
                                const vector<double> &cv) {
    return PALISADEVector(cc->EvalInnerProduct(pv.ciphertext,
                          cc->MakeCKKSPackedPlaintext(cv), pv._size), 1);
}

PALISADEVector PALISADE::vc_hadamard(const PALISADEVector &pv,
                                     const vector<double> &cv) {
    return PALISADEVector(cc->EvalMult(pv.ciphertext,
                                       cc->MakeCKKSPackedPlaintext(cv)), pv._size);
}

// Constant-Matrix Vector Operations:
PALISADEVector PALISADE::cmv_mult(vector<vector<double>> cm,
                                  PALISADEVector pv) {
    // Need to determine if the matrix size matches up with the vector
    // Otherwise, need to pad the input constant matrix with zeros
    if (int(cm[0].size()) < pv._size) {
        int size_diff = pv._size - int(cm[0].size());
        for (int i = 0; i < int(cm.size()); i++) {
            for (int j = 0; j < size_diff; j++)
                cm[i].push_back(0);
        }
    }

    PALISADEVector result = pv;

    if (cm.size() == cm[0].size()) {
        // Square matrix multiply
        // Need N-1 rotations for an N dimensional input vector
        // TODO: need to pad matrix so that it has the correct shape for the matrix multiply
        // Setting the rotation indices for the vector rotation permutations
        vector<int> index_list;
        for (int i = 1; i < pv._size; i++)
            index_list.push_back(i);
        set_rotation_indices(pv, index_list);

        // Rotating the initial vector to obtain all N vector permutations and extracting the diagonal
        // elements from the input matrix
        vector<PALISADEVector> vector_permutations;
        vector_permutations.push_back(pv);

        vector<vector<double>> diagonal_elements;
        diagonal_elements.push_back(lth_diagonal(cm, 0));

        for (int i = 1; i < pv._size; i++) {
            vector_permutations.push_back(v_rot(pv, i));
            diagonal_elements.push_back(lth_diagonal(cm, i));
        }

        vector<vector<double>> decrypted_rotations;
        for (int i = 0; i < int(vector_permutations.size()); i++)
            decrypted_rotations.push_back(decrypt_vector(vector_permutations[i], 3));

        result = vc_hadamard(vector_permutations[0], diagonal_elements[0]);
        for (int i = 1; i < int(diagonal_elements.size()); i++) {
            result = v_add(result, vc_hadamard(vector_permutations[i],
                                               diagonal_elements[i]));
        }

    } else {
        if (cm.size() > cm[0].size()) {
            // More rows than columns (lanky/skinny matrix multiply)

        } else {
            // More columns than rows (squat/wide matrix multiply)

        }
    }
    return result;
}


#endif //ETO_PALISADE_H
