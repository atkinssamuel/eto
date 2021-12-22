#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include "seal/seal.h"
#include "toy.h"

using namespace seal;
using namespace std;
namespace py = pybind11;

int ckks_test(){
    EncryptionParameters parms(scheme_type::ckks);

    size_t poly_modulus_degree = 8192;
    parms.set_poly_modulus_degree(poly_modulus_degree);
    parms.set_coeff_modulus(CoeffModulus::Create(poly_modulus_degree, {60, 40, 40, 60}));

    double scale = pow(2.0, 40);

    SEALContext context(parms);

    KeyGenerator keygen(context);
    auto secret_key = keygen.secret_key();

    PublicKey public_key;
    RelinKeys relin_keys;
    GaloisKeys gal_keys;


    keygen.create_public_key(public_key);
    keygen.create_relin_keys(relin_keys);
    keygen.create_galois_keys(gal_keys);

    Encryptor encryptor(context, public_key);
    Evaluator evaluator(context);
    Decryptor decryptor(context, secret_key);
    CKKSEncoder encoder(context);

    vector<double> vect;
    vect.reserve(encoder.slot_count());

    vect.push_back(10);
    vect.push_back(20);
    vect.push_back(30);

    Plaintext x_plain;
    encoder.encode(vect, scale, x_plain);


    Ciphertext x_encrypted;
    encryptor.encrypt(x_plain, x_encrypted);


    return 0;
}


PYBIND11_MODULE(toy, m){
    m.doc() = "pybind11 example plugin";
    m.def("ckks_test", &ckks_test);
}

