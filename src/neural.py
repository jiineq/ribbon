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



#weights = load_weights()

#Load Words
#paper = prep_paper(sys.argv[1])
#words = split_words(split_phrases(split_sentences(paper)))
#words = clean_empties(words)
#indexing = index_words(words)
#print(words)

#Matrix Form
#word_vec = Matrix(len(words), 1, vec_convert)

#weight adjustments
#weights[0] = adjust_weight_col(weights[0],word_vec.rows)
#weights[7] = adjust_weight_row(weights[7],word_vec.rows)

#print weights[7]


#print(word_vec.rows,word_vec.cols)
#print(weights[0].rows,weights[0].cols)
#print(weights[7].rows,weights[7].cols)

#end_vec = forward(word_vec)

#print end_vec

#save_weights(weights)
