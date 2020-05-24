cmake_minimum_required(VERSION 3.0.0)
project(investor_c)

add_subdirectory(pybind11)
pybind11_add_module(investor_c investor_c.cpp)

include_directories(pybind11/include)