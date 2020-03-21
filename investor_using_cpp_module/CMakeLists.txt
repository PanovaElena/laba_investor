cmake_minimum_required(VERSION 2.8.12)
project(investor_c)

add_subdirectory(pybind11)
pybind11_add_module(investor_c investor_c.cpp)

include_directories(pybind11/include)