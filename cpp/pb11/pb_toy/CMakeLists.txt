cmake_minimum_required(VERSION 3.13)
project(toy)

add_subdirectory(pybind11)
pybind11_add_module(toy toy.cpp)

find_package(SEAL)
target_link_libraries(toy PRIVATE SEAL::seal)