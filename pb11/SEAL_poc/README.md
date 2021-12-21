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

## PyBind11 Integration with CMake
The next step is to integrate SEAL and PyBind11 with CMake.


1. Create the .cpp file that will contain the intended functionality
2. Clone the PyBind11 git repository into the same folder as the .cpp file
```
git clone git@github.com:pybind/pybind11.git
```
3. Create a CMakeLists.txt file that mimics the structure of the one in this directory. Ensure to include the "PRIVATE" 
keyword in the "target_link_libraries" function (```target_link_libraries(example PRIVATE SEAL::seal)```)
6. Make the project
```
mkdir build
cd build
cmake ..
make
```

The ```.so``` file will be generated into the ```build``` directory and can be imported into a Python project.