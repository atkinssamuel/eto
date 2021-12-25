//
// Created by atkinswsl on 12/24/21.
//

#include "CKKSEncryptor.h"

CKKSEncryptor::CKKSEncryptor(size_t poly_modulus_degree, vector<int> bit_sizes, float scale_x, float scale_y):
        poly_modulus_degree(poly_modulus_degree), bit_sizes(std::move(bit_sizes)), scale_x(scale_x), scale_y(scale_y){}

size_t CKKSEncryptor::GetPolyModulusDegree() const {
    return CKKSEncryptor::poly_modulus_degree;
}

void CKKSEncryptor::SetPolyModulusDegree(size_t polyModulusDegree) {
    CKKSEncryptor::poly_modulus_degree = polyModulusDegree;
}

vector<double> CKKSEncryptor::Encrypt(vector<double> input){
    input.reserve(encoder.slot_count());

    Plaintext x_plain;
    encoder.encode(input, scale, x_plain);

    Ciphertext x_encrypted;
    encryptor.encrypt(x_plain, x_encrypted);

    decryptor.decrypt(x_encrypted, x_plain);

    vector<double> output;
    encoder.decode(x_plain, output);

    return output;
}
