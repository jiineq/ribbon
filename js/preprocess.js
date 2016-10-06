var math = require('mathjs');

function split_word(paper){
	string = paper.replace(/[^\x00-\x7F]/g, "") //Remove any non-ascii characters
	return string.split(/^\w/);
}

function hash(word){
	string = "";
	for(i = 0; i < word.length; i++)
		string += word.charCodeAt(i);
	return parseFloat(string)/math.pow(10,string.length)
}

console.log(hash("dog"))
