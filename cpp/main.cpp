//
// Created by atkinswsl on 12/22/21.
//

#include <pybind11/pybind11.h>
#include "CKKSEncryptor.h"
//#include "EncryptedData.h"

namespace py = pybind11;
#include "seal/seal.h"
using namespace seal;
using namespace std;




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

    vector<double> Encrypt(vector<double> input);
};


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

// C++ in Python the Easy Way! #pybind11 https://www.youtube.com/watch?v=_5T70cAXDJ0

PYBIND11_MODULE(CustomEncryptor, handle){
    py::class_<CKKSEncryptor>(handle, "CKKSEncryptor")
            .def(py::init<size_t, vector<int>, float, float>());
//            .def_property("poly_modulus_degree", &CKKSEncryptor::GetPolyModulusDegree, &CKKSEncryptor::SetPolyModulusDegree)
//            .def("Encrypt", &CKKSEncryptor::Encrypt);
//    py::class_<EncryptedData>(handle, "EncryptedData");
}

