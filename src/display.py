from sympy import Matrix

def genhtml(word_vec, end_vec):
	print(word_vec)
	f = open("../highlight/"+str(word_vec[0])+" "+str(word_vec[1])+".html", "w")
	f.write("<!DOCTYPE html><html><head><body>")
	for i in range(len(end_vec)):
		if(end_vec[i,0] > .85):
			f.write("<a style=\"background-color: #FFFF00;\">")
			f.write(str(word_vec[i]))
			f.write("</a> ")
		else:
			f.write(word_vec[i]+" ")
	f.write("</body></head></html>")
	f.close()

