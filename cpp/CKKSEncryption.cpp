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

CKKSEncryption::CKKSEncryption() {
    parms.set_poly_modulus_degree(poly_modulus_degree);
    parms.set_coeff_modulus(CoeffModulus::Create(poly_modulus_degree, {60, 40, 40, 60}));

    CKKSEncryption::context = SEALContext(parms);

    KeyGenerator keygen(context);
    secret_key = keygen.secret_key();

    keygen.create_public_key(public_key);
    keygen.create_relin_keys(relin_keys);
    keygen.create_galois_keys(gal_keys);

//    encryptor = Encryptor(context, public_key);
//    evaluator = Evaluator(context);
//    decryptor = Decryptor(context, secret_key);
//    encoder = CKKSEncoder(context);
}

vector<double> CKKSEncryption::Encrypt(){
    Encryptor encryptor = Encryptor(context, public_key);
    Evaluator evaluator = Evaluator(context);
    Decryptor decryptor = Decryptor(context, secret_key);
    CKKSEncoder encoder = CKKSEncoder(context);

    vector<double> vect;
    vect.reserve(encoder.slot_count());

    vect.push_back(10);
    vect.push_back(20);
    vect.push_back(30);

    Plaintext x_plain;
    encoder.encode(vect, scale, x_plain);


    Ciphertext x_encrypted;
    encryptor.encrypt(x_plain, x_encrypted);

    decryptor.decrypt(x_encrypted, x_plain);

    encoder.decode(x_plain, vect);

    return vect;
}


PYBIND11_MODULE(CKKSEncryption, handle){
    py::class_<CKKSEncryption>(handle, "CKKSEncryption")
            .def(py::init())
            .def("Encrypt", &CKKSEncryption::Encrypt);
}

