#!/usr/bin/python
from neural import *
from display import *
from sympy import Matrix


def vec_convert(i,j):
	hash_word(words[i])
weights = load_weights()

f = open(sys.argv[1],"r")
paper = prep_paper(f.read())
f.close()
words = split_words(split_phrases(split_sentences(paper)))
words = clean_empties(words)


word_vec = Matrix(len(words), 1, vec_convert)

weights[0] = adjust_weight_col(weights[0],word_vec.rows)
weights[7] = adjust_weight_row(weights[7],word_vec.rows)

end_vec = forward(word_vec, weights)

data = (words, end_vec)
genhtml(data)



