This repository uses git submodules. To download the code and the dependencies please use
```bash
git clone --recursive https://github.com/PanovaElena/laba_investor
```

The `investor_only_python` directory contains the task implementation using `numpy` and `numba`.
The `investor_using_cpp_module` directory contains the task implementation using Python as a wrapper 
and C++ as a computational core (`pybind11`). You need to build C++ module before start using `cmake`.

To start the program use:
```bash
python bonds.py -a dynamic -i input.txt -o output.txt
```

Here `input.txt` and `output.txt` are input and output files, `dynamic` is the algorithm giving an exact solution.
