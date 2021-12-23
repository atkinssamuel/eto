//
// Created by atkinswsl on 12/22/21.
//

#include "seal/seal.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

using namespace seal;
using namespace std;


class CKKSEncryption{
public:
    EncryptionParameters parms = EncryptionParameters(scheme_type::ckks);
    size_t poly_modulus_degree = 8192;
    double scale = pow(2.0, 40);

    SEALContext context = SEALContext(parms);

    PublicKey public_key;
    SecretKey secret_key;
    RelinKeys relin_keys;
    GaloisKeys gal_keys;


//    Encryptor encryptor;
//    Evaluator evaluator;
//    Decryptor decryptor;
//    CKKSEncoder encoder;

    CKKSEncryption();
    vector<double> Encrypt();
};



