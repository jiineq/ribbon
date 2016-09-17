#!/usr/bin/python
from preprocess import *
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
	for i in range(10):
		words_vec = sigmoid(w[i]*words_vec)
	return words_vec

paper = prep_paper(sys.argv[1])
words = split_words(split_phrases(split_sentences(paper)))
words = clean_empties(words)

indexing = index_words(words)
#words = clean_common(words)

print(words)

word_vec = Matrix(len(words), 1, vec_convert)

print word_vec


