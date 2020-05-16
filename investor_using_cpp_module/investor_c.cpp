#include <vector>
#include <iostream>
#include <random>
#include <chrono>
#include <algorithm>

#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

namespace py = pybind11;

struct Object {
	int weight;
	int value;

	Object(int weight = 0, int value = 0) :
		weight(weight), value(value) {}
};


struct Solution {
	int max_profit;
	std::vector<int> taken;
};


Solution solve_knapsack_problem(const std::vector<Object> objects, int W) {
	int n = objects.size();
	std::vector<std::vector<int>> m(n + 1);
	std::vector<std::vector<int>> arrpath_j(n + 1);
	for (int i = 0; i < n + 1; i++) {
		m[i].resize(W + 1);
		arrpath_j[i].resize(W + 1);
	}

	for (int i = 1; i < n + 1; i++)
		for (int j = 0; j < W + 1; j++) {
			int wi = objects[i - 1].weight;
			int vi = objects[i - 1].value;
			if (wi > j)
				m[i][j] = m[i - 1][j];
			else
				m[i][j] = std::max(m[i - 1][j], m[i - 1][j - wi] + vi);
			if (m[i][j] == m[i - 1][j])
				arrpath_j[i][j] = j;
			else
				arrpath_j[i][j] = j - wi;
		}

	Solution s;

	int cur_j = W;
	for (int i = n; i > 0; i--)
		if (cur_j != arrpath_j[i][cur_j]) {
			s.taken.push_back(i - 1);
			cur_j = arrpath_j[i][cur_j];
		}

	s.max_profit = m[n][W];

	return s;
}


PYBIND11_MODULE(investor_c, object) {

	py::class_<Object>(object, "Object")
		.def(py::init<int, int>())
		.def_readwrite("weight", &Object::weight)
		.def_readwrite("value", &Object::value)
		;

	py::class_<Solution>(object, "SolutionKnapsackProblem")
		.def_readwrite("max_profit", &Solution::max_profit)
		.def_readwrite("taken", &Solution::taken)
		;

	object.def("solve_knapsack_problem", &solve_knapsack_problem);

}


