#!/usr/bin/python
from sympy import Matrix, eye
from sympy.matrices import randMatrix
from random import *

def load_weights():
	weights = [0,0,0,0,0,0,0,0]
	for i in range(8):
		try:
			f = open("../weights/weight" + str(i), "r")
			content =  f.read().split(",")
			def readmatrix(i,j):
				return content[i*5+j]
		
			weights[i] = Matrix(5,5,readmatrix)
			f.close()
		except:
			weights[i] = randMatrix(5,5,1,9999)/10000.0
	return weights

def save_weights(weights):	
	for i in range(8):
		#print weights[i]
		f = open("../weights/weight" + str(i), "w")
		for j in range(5):
			for k in range(5):
				f.write(str(weights[i][j,k]) + ',')
		f.close()
def mutate(weight, rate, direction):
	for i in range(weight.rows):
		for j in range(weight.cols):
			if(direction == 1):
				weight[i,j] = (1+(random()*rate)) * weight[i,j]
			elif(direction == -1):
				weight[i,j] = (1-(random()*rate)) * weight[i,j]
	return weight


def adjust_weight_row(weight, new_size):
	diff = new_size - weight.rows
	original_size = weight.rows
	for i in range(diff):
		new_row = weight[i%(original_size):i%(original_size)+1,0:5]
		weight = Matrix([weight,new_row])
	#	print(weight)
	return weight

def adjust_weight_col(weight, new_size):
	diff = new_size - weight.cols
	original_size = weight.cols
	for i in range(diff):
		new_col = weight.transpose()[i%(original_size):i%(original_size)+1,0:5]
		weight = Matrix([weight.transpose(),new_col]).transpose()
	#	print(weight)
	return weight

def resize(weight):
	return weight[0:5,0:5]

#weights = load_weights()
#adjust_weight_row(weights[0],13)
#adjust_weight_col(weights[7],15)

#save_weights(load_weights())
