#include <pybind11/pybind11.h>
#include "seal/seal.h"

using namespace seal;
using namespace std;
namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

int bfv_basics(){
    EncryptionParameters parms(scheme_type::bfv);
    size_t poly_modulus_degree = 4096;
    parms.set_poly_modulus_degree(poly_modulus_degree);
    parms.set_coeff_modulus(CoeffModulus::BFVDefault(poly_modulus_degree));
    parms.set_plain_modulus(1024);
    return 0;
}


PYBIND11_MODULE(example, m){
    m.doc() = "pybind11 example plugin";
    m.def("add", &add, "A function which adds two numbers");
    m.def("bfv_basics", &bfv_basics, "A function which adds two numbers");

}

