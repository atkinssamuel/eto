cmake_minimum_required(VERSION 3.13)
project(cpp)

add_subdirectory(pybind11)
pybind11_add_module(CKKSEncryption CKKSEncryption.cpp)

find_package(SEAL)
target_link_libraries(CKKSEncryption PRIVATE SEAL::seal)