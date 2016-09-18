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
	#	print(weights[i].rows,weights[i].cols, words_vec.rows, words_vec.cols)
		words_vec = weights[i] * words_vec
		for j in range(words_vec.rows):
			for k in range(words_vec.cols):
				words_vec[j,k] = sigmoid(words_vec[j,k])
		
	return words_vec



weights = load_weights()

#Load Words
f = open(sys.argv[1],"r")
paper = prep_paper(f.read())
f.close()
words = split_words(split_phrases(split_sentences(paper)))
words = clean_empties(words)
#indexing = index_words(words)
#print(words)

#Matrix Form
word_vec = Matrix(len(words), 1, vec_convert)

#weight adjustments
weights[0] = adjust_weight_col(weights[0],word_vec.rows)
weights[7] = adjust_weight_row(weights[7],word_vec.rows)

#print weights[7]


#print(word_vec.rows,word_vec.cols)
#print(weights[0].rows,weights[0].cols)
#print(weights[7].rows,weights[7].cols)

end_vec = forward(word_vec, weights)

print end_vec

genhtml(words, end_vec)
print("done")

#save_weights(weights)
