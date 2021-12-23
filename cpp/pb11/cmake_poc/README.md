fin# PyBind11 with CMake
## Installation Guide
1. Create the .cpp file that will contain the intended functionality
2. Clone the PyBind11 git repository into the same folder as the .cpp file
```
git clone git@github.com:pybind/pybind11.git
```
3. Create a CMakeLists.txt file that mimics the structure of the one in this directory
4. Make the project
```
mkdir build
cd build
cmake ..
make
```

The ```.so``` file will be generated into the ```build``` directory and can be imported into a Python project.