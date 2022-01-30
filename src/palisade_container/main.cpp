//
// Created by atkinswsl on 12/22/21.
//

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

#include <utility>
#include "PALISADE.h"

namespace py = pybind11;
using namespace lbcrypto;

// C++ in Python the Easy Way! #pybind11 https://www.youtube.com/watch?v=_5T70cAXDJ0
PYBIND11_MODULE(PALISADEContainer, handle) {
    py::class_<PALISADE>(handle, "PALISADEContainer")
    .def(py::init<uint32_t, uint32_t, uint32_t>())
    .def("encrypt_vector", &PALISADE::encrypt_vector)
    .def("decrypt_vector", &PALISADE::decrypt_vector)
    .def_property_readonly("embedding_size", &PALISADE::embedding_size)
    .def("v_hadamard", &PALISADE::v_hadamard) // Vector-Vector Operations
    .def("set_rotation_vector_indices", &PALISADE::set_rotation_vector_indices)
    .def("v_dot", &PALISADE::v_dot)
    .def("v_add", &PALISADE::v_add)
    .def("v_sum", &PALISADE::v_sum)
    .def("v_rot", &PALISADE::v_rot)
    .def("vc_dot", &PALISADE::vc_dot);
//            .def("matrix_add", &PALISADE::matrix_add);

    py::class_<PALISADEVector>(handle, "PALISADEVector")
    .def_property_readonly("size", &PALISADEVector::size)
    .def_property_readonly("unpadded_size", &PALISADEVector::unpadded_size);


    handle.doc() = "pybind11";
}
