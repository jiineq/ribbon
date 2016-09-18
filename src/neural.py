#!/usr/bin/python
from preprocess import *
from weights import *
from math import *
from sympy import Matrix

def vec_convert(i,j):
	return hash_word(words[i])

def sigmoid(x):
	return (1.0)/(1 + e**(-x))

def ddxsigmoid(x):
	return sigmoid(x) * (1 - sigmoid(x))

def hash_word(word):
	string = ""
	for c in word:
		string += str(ord(c))
	return float(string)/10**(len(string))

def forward(words_vec):
	for i in range(8):
		words_vec = sigmoid(weights[i]*words_vec)
	return words_vec



weights = load_weights()

#Load Words
paper = prep_paper(sys.argv[1])
words = split_words(split_phrases(split_sentences(paper)))
words = clean_empties(words)
indexing = index_words(words)
#print(words)

#Matrix Form
word_vec = Matrix(len(words), 1, vec_convert)

#print weights[0]
values = []
print(word_vec.rows)
for i in range(word_vec.rows):
	for j in range(5):
		values.append(weights[0][i%weights[0].rows,j])
print values
weights[0] = Matrix(word_vec.rows, 5, values)
print weights[0]

values = []
for i in range(word_vec.cols):
	for j in range(5):
		values.append(weights[7].transpose()[i%weights[7].transpose().cols,j])
weights[7] = Matrix(5, word_vec.cols, values)


word_vec = forward(word_vec)

print word_vec

