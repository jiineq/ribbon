#!/usr/bin/python
from neural import *
from display import *
from sympy import Matrix

def hash_word(word):
	string = ""
	for c in word:
		string += str(ord(c))
	return float(string)/10**(len(string))



def process():
	average_err = 1
	while(abs(average_err) > .15):
		def vec_convert(i,j):
			return hash_word(words[i]) 
		for j in range(len(weights)):
			#print(weights[j])
			weights[j] = mutate(weights[j], .05)
		start = open("../training/art"+str(i+1)+"_raw.txt", "r")
		paper = prep_paper(start.read())
		start.close()
		words = clean_empties(split_words(split_phrases(split_sentences(paper))))
		num_words = len(words)
		words_vec = Matrix(len(words), 1, vec_convert)
		
		weights[0] = adjust_weight_col(weights[0], words_vec.rows)
		weights[7] = adjust_weight_row(weights[7], words_vec.rows)
	
		end_vec = forward(words_vec, weights)
		end = open("../training/art"+str(i+1)+"_Y.txt", "r")
		
		y = end.read().split(",")
		end.close()
		average_err = 0.0
		for j in range(len(y)):
			average_err += float(float(y[i])-end_vec[i])
	
		average_err = average_err / float(num_words)
		print("Average Error: " + str(average_err))
		weights[0] = resize(weights[0])
		weights[7] = resize(weights[7])
	return(words, end_vec)

weights = load_weights()


for i in range(3):
	vecs = process()
	genhtml(vecs[0],vecs[1])

save_weights(weights)	


