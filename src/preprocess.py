#!/usr/bin/python
import sys

def prep_paper(paper):
	return paper.strip().replace("?",".").replace("!",".").upper()

def split_sentence(paper):
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

def clean_empties(string_list):
	return filter(lambda a: a != '', string_list)

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

paper = sys.argv[1]
paper = prep_paper(paper)
sentences = split_sentence(paper)
phrases = split_phrases(sentences)
words = split_words(phrases)
words = clean_empties(words)
print (words)
print ("Table:");
print(frequency_table(words))
