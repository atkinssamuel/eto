//
// Created by atkinswsl on 12/22/21.
//

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>


#include "CKKSEncryptor.h"
#include "MatrixCiphertextContainer.h"

namespace py = pybind11;

// C++ in Python the Easy Way! #pybind11 https://www.youtube.com/watch?v=_5T70cAXDJ0

PYBIND11_MODULE(CustomEncryptor, handle){
    py::class_<CKKSEncryptor>(handle, "CKKSEncryptor")
            .def(py::init<size_t, vector<int>, float, float>())
            .def_property("poly_modulus_degree", &CKKSEncryptor::GetPolyModulusDegree, &CKKSEncryptor::SetPolyModulusDegree)
            .def("DecryptVector", &CKKSEncryptor::DecryptVector);

    py::class_<MatrixCiphertextContainer>(handle, "MatrixCiphertextContainer");
//            .def(py::init<CKKSEncryptor&>())
//            .def("Encrypt", &MatrixCiphertextContainer::Encrypt)
//            .def("Decrypt", &MatrixCiphertextContainer::Decrypt);
}

