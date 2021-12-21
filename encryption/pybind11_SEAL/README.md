# SEAL Integration with PyBind11
## SEAL Installation
https://github.com/Microsoft/SEAL#installing-microsoft-seal  

The first step in integrating SEAL with PyBind11 is ensuring that SEAL can be built and run properly. The following is 
a step-by-step guide on how to set up Microsoft SEAL on Linux:

1. Clone Microsoft SEAL into the repository that you will be working in
```
git clone git@github.com:microsoft/SEAL.git
```
2. Install g++ (>= 6.0) and CMake (>= 3.13)
```
sudo apt update
sudo apt install g++
sudo apt install cmake
```
3. Globally install Microsoft SEAL
```
cd SEAL
cmake -S . -B build
cmake --build build
sudo cmake --install build
```

## C++ Program Compilation with G++
The next step is learning how to include the SEAL library into a simple C++ program without using CMake. 