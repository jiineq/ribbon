#!/usr/bin/python
from display import *
from preprocess import *
from neural import *
from weights import *
import os
from sympy import Matrix

weights = load_weights()
total_len = 0



def think(word_vecs, results, weights, num_generations):
	for i in range(num_generations):
		print("Generation "+str(i))
		#mutate Weights
		print("\tMutating Weights...")
		mutants = []
		for j in range(50):
			mutant = []
			for k in range(len(weights)):
				mutant.append(mutate(weights[k], .05))
			mutants.append(mutant)
		mutants.append(weights)
		
		#find the average error that one mutant has to every paper
		print("\tCalculating Errors...")
		errors = []
		for j in range(len(mutants)):
			print("\t\tMutant No. " + str(j))
			end_vecs = []
			error = 0.0
			for k in range(len(word_vecs)):
				print("\t\t\tPaper No. " + str(k))
				mutants[j][0] = adjust_weight_col(mutants[j][0], word_vecs[k].rows)
				mutants[j][7] = adjust_weight_row(mutants[j][7], word_vecs[k].rows)
				end_vec = forward(word_vecs[k], mutants[j])
				for l in range(len(results[k])):
					error += float(results[k][l]) - end_vec[i,0]
				mutants[j][0] = resize(mutants[j][0])
				mutants[j][7] = resize(mutants[j][7])
	
			error = error / float(total_len)
			errors.append(error)

		
		print("\tSearching for most \"fit\" mutant")
		min_error = (errors[0],0)
		for j in range(len(errors)):
			if(abs(errors[j]) < abs(min_error[0])):
				min_error = (errors[j], j)
		best_mutant = mutants[j]
		print("\tFittest's Mutant's Error: " + str(min_error[0]))
		weights = best_mutant	
	save_weights(weights)

#Read all files
papers = []
for dirpath, dnames, fnames in os.walk("../training/samples"):
	for f in fnames:
		a_file = open(os.path.join(dirpath,f), "r")
		content = a_file.read()

		papers.append(content)
		total_len += len(content)
	
		a_file.close()

results = []
for dirpath, dnames, fnames in os.walk("../training/answers"):
	for f in fnames:
		a_file = open(os.path.join(dirpath,f),"r")
		results.append(a_file.read().split(","))
		a_file.close()


#Prepare/parse all files into vector form
for i in range(len(papers)):
	papers[i] = clean_empties(split_words(split_phrases(split_sentences(prep_paper(papers[i])))))
	papers[i] = word_vec_convert(papers[i])

think(papers, results, weights, 100)
