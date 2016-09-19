
var in = "";

function toarray(words) {
	words = words.split(" ");
	
	var array = [];
	
	for(var i = 0; i < words.length; i++) {
		if(words[i].includes("`")) {
			array.push(1);
		} else {
			array.push(0);
		}
	}
	
	return array;
}