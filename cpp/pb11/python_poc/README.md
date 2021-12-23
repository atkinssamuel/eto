# PyBind11 POC
## Setup Guide:
https://pybind11.readthedocs.io/en/stable/basics.html  
https://www.youtube.com/watch?v=MNBpFtliZIQ 

1. Install pybind11 using Python  
```
conda install -c conda-forge pybind11
```
2. Install python3-dev, cmake, and g++
```
sudo apt update
sudo apt install python3-dev
sudo apt install cmake
sudo apt install g++
```
3. Make a file that mimics the structure of the ```example.cpp``` file in this directory
4. Build the library
```
c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) example.cpp -o example$(python3-config --extension-suffix)
```

The functionality defined in the .cpp file will now be exposed in Python. To import the "example" library, include an 
```__init__.py``` file in the directory that contains the ```.so``` file and then import the library:

```
from pybind11_poc import example
```