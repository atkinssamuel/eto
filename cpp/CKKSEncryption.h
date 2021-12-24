//
// Created by atkinswsl on 12/22/21.
//

#include "seal/seal.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

using namespace seal;
using namespace std;

EncryptionParameters GetParams(){
    size_t poly_modulus_degree = 8192;
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

class CKKSEncryption{
public:
    double scale = pow(2.0, 40);
    EncryptionParameters parms = GetParams();

    SEALContext context = SEALContext(parms);

    PublicKey public_key;
    RelinKeys relin_keys;
    GaloisKeys gal_keys;
    SecretKey secret_key = InitKeys(context, &public_key, &relin_keys, &gal_keys);


    Encryptor encryptor = Encryptor(context, public_key);
    Decryptor decryptor = Decryptor(context, secret_key);
    Evaluator evaluator = Evaluator(context);
    CKKSEncoder encoder = CKKSEncoder(context);


    CKKSEncryption();
    vector<double> Encrypt(vector<double> input);
};



