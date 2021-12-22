//
// Created by atkinswsl on 12/22/21.
//

#include "CKKSEncryption.h"
#include <pybind11/pybind11.h>
#include "seal/seal.h"

using namespace seal;
using namespace std;
namespace py = pybind11;



PYBIND11_MODULE(encrypted_operations, m){
    m.doc() = "CKKS Encryption Class";
    m.def("add", &add, "A function which adds two numbers");
    m.def("bfv_basics", &bfv_basics, "A function which adds two numbers");

}

