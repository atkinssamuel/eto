//
// Created by atkinswsl on 12/22/21.
//

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

#include <utility>
#include "palisade.h"
#include "PALISADE.h"

namespace py = pybind11;
using namespace lbcrypto;


void palisade_example(){
    PALISADE palisade = PALISADE();
    vector<double> x = {1.0, 2.0, 3.0, 4.0};

    vector<PALISADEVector> pm;
    pm.push_back(palisade.encrypt_vector(x));


}

// C++ in Python the Easy Way! #pybind11 https://www.youtube.com/watch?v=_5T70cAXDJ0
PYBIND11_MODULE(PALISADEContainer, handle){
    py::class_<PALISADE>(handle, "PALISADE")
            .def(py::init())
            .def("encrypt_vector", &PALISADE::encrypt_vector)
            .def("decrypt_vector", &PALISADE::decrypt_vector)
            .def("v_hadamard", &PALISADE::v_hadamard) // Vector-Vector Operations
            .def("v_dot", &PALISADE::v_dot)
            .def("v_add", &PALISADE::v_add)
            .def("v_sum", &PALISADE::v_sum)
            .def("vc_dot", &PALISADE::vc_dot);
//            .def("matrix_add", &PALISADE::matrix_add);

    py::class_<PALISADEVector>(handle, "PALISADEVector");
    handle.def("palisade_example", &palisade_example);

    handle.doc() = "pybind11";
}
