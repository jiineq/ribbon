#!/usr/bin/python
from preprocess import *
from weights import *
from math import *
from display import *
from sympy import Matrix

def vec_convert(i,j):
	return hash_word(words[i])

def sigmoid(x):
	return (1.0)/(1.0 + e**(-x))

def ddxsigmoid(x):
	return sigmoid(x) * (1 - sigmoid(x))

def hash_word(word):
	string = ""
	for c in word:
		string += str(ord(c))
	return float(string)/10**(len(string))

def forward(words_vec, weights):
	for i in range(8):
		words_vec = weights[i] * words_vec
		for j in range(words_vec.rows):
			for k in range(words_vec.cols):
				words_vec[j,k] = sigmoid(words_vec[j,k])
		
	return words_vec



weights = load_weights()

#Load Words
f = open(sys.argv[1],"r")
paper = f.read()
punctuation = get_punctuation(paper)
caps = get_caps(paper)
paper = prep_paper(paper)
f.close()
words = split_words(split_phrases(split_sentences(paper)))
words = clean_empties(words)

#Matrix Form
word_vec = Matrix(len(words), 1, vec_convert)

#weight adjustments
weights[0] = adjust_weight_col(weights[0],word_vec.rows)
weights[7] = adjust_weight_row(weights[7],word_vec.rows)

end_vec = forward(word_vec, weights)

#print end_vec
compose(words, end_vec, caps, punctuation)

print("done")
