# SEAL Integration with PyBind11
## SEAL Installation
https://github.com/Microsoft/SEAL#installing-microsoft-seal  

The first step in integrating SEAL with PyBind11 is ensuring that SEAL can be built and run properly. The following is 
a step-by-step guide on how to set up Microsoft SEAL on Linux:

1. Clone Microsoft SEAL 
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
4. Remove the SEAL directory

*NOTE:*  
By default SEAL declares the Encryptor, Evaluator, and Decryptor classes as non-copyable. This prevents one 
from creating Encryptor, Evaluator, and Decryptor members for a custom class. To rectify this problem, the 
following files were edited:

```
/usr/local/include/SEAL-3.7/seal/encryptor.h
/usr/local/include/SEAL-3.7/seal/evaluator.h
/usr/local/include/SEAL-3.7/seal/keygenerator.h

```

The "= delete" restrictions on the copy, source, constant assign, and assign methods were commented out in the private 
section of each class. This will allow us to copy the encryptor and evaluator objects to our own CKKS encryption class. 
The decryptor class was left as non-copyable because the non-copyable nature of this class is deeply embedded in SEAL. 
The decryptor class will be instantiated everytime we wish to decrypt something.

## PyBind11 Integration with CMake
The next step is to integrate SEAL and PyBind11 with CMake.


1. Create the .cpp file that will contain the intended functionality
2. Clone the PyBind11 git repository into the same folder as the .cpp file
```
git clone git@github.com:pybind/pybind11.git
```
3. Create a CMakeLists.txt file that mimics the structure of the one in this directory. Ensure to include the "PRIVATE" 
keyword in the "target_link_libraries" function (```target_link_libraries(example PRIVATE SEAL::seal)```)
4. Make the project
```
mkdir build
cd build
cmake ..
make
```

The ```.so``` file will be generated into the ```build``` directory and can be imported into a Python project.