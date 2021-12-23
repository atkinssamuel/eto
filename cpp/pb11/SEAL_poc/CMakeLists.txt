cmake_minimum_required(VERSION 3.13)
project(example)

add_subdirectory(pybind11)
pybind11_add_module(example example.cpp)

find_package(SEAL)
target_link_libraries(example PRIVATE SEAL::seal)