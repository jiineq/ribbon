#!/usr/bin/python
from math import *
from sympy import Matrix

def sigmoid(x):
	return (1.0)/(1.0 + e**(-x))

def ddxsigmoid(x):
	return sigmoid(x) * (1 - sigmoid(x))

def forward(words_vec, weights):
	for i in range(8):
		words_vec = weights[i] * words_vec
		for j in range(words_vec.rows):
			for k in range(words_vec.cols):
				words_vec[j,k] = sigmoid(words_vec[j,k])		
	return words_vec

