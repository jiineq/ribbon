#!/usr/bin/python
from neural import *
from sympy import Matrix

weights = load_weights()
average_err = 1

for i in range(10):
	while(average_err > .15):
		for j in len(weights):
			weights[j] = mutate(weights[j], .05)
		start = open("../training/test"+str(i)+".start", "r")
		paper = prep_paper(start.read())
		words = clean_empties(split_words(split_phrases(split_sentences(paper))))
		num_words = len(words)
		word_vec = Matrix(len(words), 1, vec_convert)
		
		weights[0] = adjust_weight_col(weights[0], words_vec.rows)
		weights[7] = adjust_weight_row(weights[7], words_vec.rows)
	
		end_vec = forward(word_vec)
		end = open("../training/test"+str(i)+".end", "r")
		
		y = end.read().split(",")
		average_err = 0.0
		for j in range(len(y)):
			average_err += float(y[i]-end_vec[i])
	
		average_err = average_err / float(num_words)
		print("Average Error: " + str(average_err))
		weight[0] = resize(weight[0])
		weight[7] = resize(weight[7])

save_weights(weights)	


