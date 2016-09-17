#!/usr/bin/python
from sympy import Matrix, eye


weights = [0,0,0,0,0,0,0,0]
for i in range(1,7):
	try:
		f = open("./weight" + str(i), "r")
		content =  f.read().split(",")
		def readmatrix(i,j):
			return content[i*5+j]
	
		weights[i] = Matrix(5,5,readmatrix)
	except:
		weights[i] = eye(5)

for i in range(1,7):
	print weights[i]
	f = open("./weight" + str(i), "w")
	for j in range(5):
		for k in range(5):
			f.write(str(weights[i][j,k]) + ',')
