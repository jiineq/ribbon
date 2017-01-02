from sympy import Matrix

def compose(words,end_vec, capitals, punct):
	print(capitals)
	f = open("../highlight/"+str(words[0])+" "+str(words[1])+".html", "w")
	f.write("<!DOCTYPE html><html><head><style>a{background-color: #FFFF00;}</style></head><body>")
	char_count = 0
	for i in range(len(words)):
		words[i] = words[i].lower()
		for c in words[i]:
			if(char_count == capitals[0]):
				word = ""
				for j in range(len(words[i])):
					if(j != char_count-capitals[0]):
						word+=words[i][j]
					else:
						word+=words[i][j].upper()
				words[i] = word
			
				capitals.pop(0)
			if(char_count == punct[0][1]):
				words[i] += punct[0][0]
				punct.pop(0)
				char_count += 1
			char_count += 1
		if(end_vec[i,0] > .9):
			f.write("<a>")
			f.write(words[i])
			f.write("</a>")
		else:
			f.write(words[i]+" ")
	f.write("</body></html>")
	f.close()
"""			

def genhtml(word_vec, end_vec):
	print(word_vec)
	f = open("../highlight/"+str(word_vec[0])+" "+str(word_vec[1])+".html", "w")
	f.write("<!DOCTYPE html><html><head><body>")
	for i in range(len(end_vec)):
		if(end_vec[i,0] > .9):
			f.write("<a style=\"background-color: #FFFF00;\">")
			f.write(str(word_vec[i]))
			f.write("</a> ")
		else:
			f.write(word_vec[i]+" ")
	f.write("</body></head></html>")
	f.close()

"""
