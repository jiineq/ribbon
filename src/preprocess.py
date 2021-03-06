#!/usr/bin/python
import sys
from sympy import zeros

common_words = ["THE", "BE", "TO", "OF", "AND", "A", "IN", "THAT", "HAVE", "I", "IT", "FOR", "NOT", "ON", "WITH", "HE", "AS", "YOU", "DO", "AT", "THIS", "BUT", "HIS", "BY", "FROM", "THEY", "WE", "SAY", "HER", "SHE", "OR", "AN", "WILL", "MY", "ONE", "ALL", "WOULD", "THERE", "THEIR", "WHAT", "SO", "UP", "OUT", "IF", "ABOUT", "WHO", "GET", "WHICH", "GO", "ME", "WHEN", "MAKE", "CAN", "LIKE", "TIME", "NO", "JUST", "HIM", "KNOW", "TAKE", "PEOPLE", "INTO", "YEAR", "YOUR", "GOOD", "SOME", "COULD", "THEM", "SEE", "OTHER", "THAN", "THEN", "NOW", "LOOK", "ONLY", "COME", "ITS", "OVER", "THINK", "ALSO", "BACK", "AFTER", "USE", "TWO", "HOW", "OUR", "WORK", "FIRST", "WELL", "WAY", "EVEN", "NEW", "WANT", "BECAUSE", "ANY", "THESE", "GIVE", "DAY", "MOST", "US"]

def get_punctuation(paper):
	punct_list = []
	i = 0
	for char in paper:
		c = ord(char)
		if (c >= 33 and c <= 47) or (c >= 58 and c <= 64) or (c >=91 and c <=96) or (c >= 123 and c <=126):
			punct_list.append((char, i))
		i = i +1
	return punct_list

def get_caps(paper):
	caps = []
	i = 0
	for char in paper:
		c = ord(char)
		if(c >= 65 and c <= 90):
			caps.append(i)
		i = i+1
	return caps

def prep_paper(paper):
	return paper.strip().replace("?",".").replace("!",".").upper()

def split_sentences(paper):
	return paper.split(".")

def split_phrases(sentences):
	phrases = []
	for sentence in sentences:
		some_phrase = sentence.replace(";",",").split(",")
		for i in range(len(some_phrase)):
			phrases.append(some_phrase[i])
	return phrases

def split_words(phrases):
	words = []
	for phrase in phrases:
		some_word = phrase.split(" ")
		for i in range(len(some_word)):
			words.append(some_word[i]);
	return words

#TODO this is dumb
def index_words(words):
	indexing = []
	for i in range(len(words)):
		indexing.append((words[i],i))
	return indexing

def clean_empties(string_list):
	return filter(lambda a: a != '', string_list)

def clean_common(words):
	for common in common_words:
		while common in words: words.remove(common)
	return words

def frequency_table(words):
	keys = []
	value = []
	for word in words:
		new_word = True
		for i in range(len(keys)):
			if(word == keys[i]):
				value[i] += 1
				new_word = False
				break;
		if(new_word):
			keys.append(word)
			value.append(1)
	#create tuples
	table = []
	for i in range(len(keys)):
		table.append((keys[i],value[i]))	
	return table

def hash_word(word):
	string = ""
	for c in word:
		string += str(ord(c))
	return float(string)/10**(len(string))

def word_vec_convert(words):
	vector = zeros(len(words), 1)
	for i in range(len(words)):
		vector[i,0] = hash_word(words[i])
	return vector

