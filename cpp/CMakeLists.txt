cmake_minimum_required(VERSION 3.13)
project(encrypted_operations)

add_subdirectory(pybind11)
pybind11_add_module(encrypted_operations encrypted_operations.cpp)

find_package(SEAL)
target_link_libraries(encrypted_operations PRIVATE SEAL::seal)