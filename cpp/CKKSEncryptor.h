//
// Created by atkinswsl on 12/24/21.
//
#include "seal/seal.h"
#include "MatrixCiphertextContainer.h"
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

using namespace seal;
using namespace std;
namespace py = pybind11;



EncryptionParameters GetParams(size_t poly_modulus_degree, const vector<int>& bit_sizes){
    EncryptionParameters parms(scheme_type::ckks);
    parms.set_poly_modulus_degree(poly_modulus_degree);
    parms.set_coeff_modulus(CoeffModulus::Create(poly_modulus_degree, {60, 40, 40, 60}));
    return parms;
}

SecretKey InitKeys(const SEALContext& context, PublicKey* public_key, RelinKeys* relin_keys, GaloisKeys* gal_keys){
    KeyGenerator keygen = KeyGenerator(context);
    keygen.create_public_key(*public_key);
    keygen.create_relin_keys(*relin_keys);
    keygen.create_galois_keys(*gal_keys);
    return keygen.secret_key();
}


class CKKSEncryptor{
public:
    size_t poly_modulus_degree;
    vector<int> bit_sizes;
    float scale_x;
    float scale_y;
    CKKSEncryptor(size_t poly_modulus_degree, vector<int> bit_sizes, float scale_x, float scale_y);

    double scale = pow(scale_x, scale_y);
    EncryptionParameters parms = GetParams(poly_modulus_degree, bit_sizes);

    SEALContext context = SEALContext(parms);

    PublicKey public_key;
    RelinKeys relin_keys;
    GaloisKeys gal_keys;
    SecretKey secret_key = InitKeys(context, &public_key, &relin_keys, &gal_keys);


    Encryptor encryptor = Encryptor(context, public_key);
    Decryptor decryptor = Decryptor(context, secret_key);
    Evaluator evaluator = Evaluator(context);
    CKKSEncoder encoder = CKKSEncoder(context);


    size_t GetPolyModulusDegree() const;
    void SetPolyModulusDegree(size_t polyModulusDegree);

    MatrixCiphertextContainer EncryptMatrix(std::vector<std::vector<float>> matrix);
    std::vector<std::vector<float>> DecryptMatrix(MatrixCiphertextContainer matrix);

    MatrixCiphertextContainer AddMatrices(MatrixCiphertextContainer A, MatrixCiphertextContainer B);
    MatrixCiphertextContainer SubtractMatrices(MatrixCiphertextContainer A, MatrixCiphertextContainer B);
    MatrixCiphertextContainer MultiplyMatrices(MatrixCiphertextContainer A, MatrixCiphertextContainer B);
};

/*
 * Setup Implementations:
 * These implementations are for the instantiation of the encryption class
 */
CKKSEncryptor::CKKSEncryptor(size_t poly_modulus_degree, vector<int> bit_sizes, float scale_x, float scale_y):
        poly_modulus_degree(poly_modulus_degree), bit_sizes(std::move(bit_sizes)), scale_x(scale_x), scale_y(scale_y){}

size_t CKKSEncryptor::GetPolyModulusDegree() const {
    return CKKSEncryptor::poly_modulus_degree;
}

void CKKSEncryptor::SetPolyModulusDegree(size_t polyModulusDegree) {
    CKKSEncryptor::poly_modulus_degree = polyModulusDegree;
}



/*
 * Encrypt/Decrypt:
 */
//MatrixCiphertextContainer EncryptMatrix(std::vector<std::vector<float>> matrix){
//
//}

