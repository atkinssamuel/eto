//
// Created by atkinswsl on 12/22/21.
//

#include <pybind11/pybind11.h>
#include "seal/seal.h"
#include "CKKSEncryption.h"
using namespace seal;
using namespace std;
namespace py = pybind11;

// C++ in Python the Easy Way! #pybind11 https://www.youtube.com/watch?v=_5T70cAXDJ0

CKKSEncryption::CKKSEncryption() = default;

vector<double> CKKSEncryption::Encrypt(vector<double> input){
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




PYBIND11_MODULE(CKKSEncryption, handle){
    py::class_<CKKSEncryption>(handle, "CKKSEncryption")
            .def(py::init())
            .def("Encrypt", &CKKSEncryption::Encrypt);
}

