This repository uses git submodules. To download the code and the dependencies please use
```bash
git clone --recursive https://github.com/PanovaElena/laba_investor
```

The `investor_base_python` directory contains the base version of the task.

The `investor_only_python` directory contains the task implementation using `numba`.

The `investor_using_cpp_module` directory contains the task implementation using Python as a wrapper 
and C++ as a computational core (`pybind11`). You need to build C++ module before start using `cmake`.


To build C++ module with `cmake` use

```bash
mkdir investor_using_cpp_module/build
cd investor_using_cpp_module/build
cmake ../ -DPYTHON_EXECUTABLE:FILEPATH=<python_path>
cmake --build ./ --config Release
```
Use generator (`-G`) for Windows and Visual Studio.
For example, `cmake ../ -DPYTHON_EXECUTABLE:FILEPATH=<python_path> -G "Visual Studio 15 2017 Win64"` for Visual Studio 2017 (x64).

To start the program use:
```bash
python bonds.py -a dynamic -i input.txt -o output.txt
```

Here `input.txt` and `output.txt` are input and output files, `dynamic` is the algorithm giving an exact solution.
