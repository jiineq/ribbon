#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "parse.h"

int is_symbol(char a)
{
	return (a>32 && a<48) || (a>57 && a<65) || (a>90 && a<97) || (a>122 && a<126);
}

int is_nonprintable(char a)
{
	return (a>0 && a<32) || a==127;
}

int contains_symbol(char* a)
{
	int i;
	for(i=0;a[i];i++)
		if(is_symbol(a[i]))
			return i;
	return -1;
}

int contains_nonprintable(char* a)
{
	int i;
	for(i=0;a[i];i++)
		if(is_nonprintable(a[i]))
			return i;
	return -1;
}

char* read_file(const char* filename)
{
	FILE* file = fopen(filename, "r");
	if(file == NULL)
	{
		printf("Cannot open file %s", filename);
		exit(0);
	}

	//Loads content of file into char*
	char* input = NULL;
	int size = 0;
	char buff[512];
	while(fgets(buff,512,file)!=NULL)
	{
		size += 512;
		input = realloc(input, size);
		strcat(input, buff);
	}
	
	return input;
}

Text* parse_input(const char* filename)
{
	char* input = read_file(filename);
	Text* text = malloc(sizeof(Text));

	//loads into struct by each word
	char** words = NULL;
	words = malloc(sizeof(char*)*512); //mem for 512 words
	int size = 0;
	char* word = strtok(input, " ");
	while(word != NULL)
	{
		int word_size = strlen(word)+1;
		char* buff = malloc(word_size);
		char* buff_start = buff;

		//symbol removal
		int index = contains_symbol(word);
		int start = index;
		if(index > -1)
		{
			word_size--;
			//cpy up to the symbol
			strncpy(buff, word, index);

			//start word after symbol
			word += index+1;
			index = contains_symbol(word);

			//Repeat for multiple symbols in a word
			//e.g. state-of-the-art
			while(index > -1)
			{
				start += index;
				word_size--;
				strncpy(buff+index, word, index);
				word += index+1; 
				index = contains_symbol(word);
			}
			//Copy last piece of word in
			strncpy(buff+start, word, strlen(word));
			buff[word_size-1] = '\0';
		}else
		{	
			strcpy(buff, word);
		}
		
		//Non-printable characters removal
		index = contains_nonprintable(buff);
		words[size] = malloc(word_size);
		if(index > -1)
		{
			while(index > -1)
			{
				word_size--;
				strncat(words[size], buff, index);
				buff += index+1;
				index = contains_nonprintable(buff);
			}
			words[size] = realloc(words[size], word_size);
		}else
		{
			strcpy(words[size], buff);
		}
		free(buff_start);
		size++;
		if(size%512==0)
		{
			words = realloc(words, size+512);
		}
		word = strtok(NULL, " ");
	}
	free(input);

	text->size = size;
	text->input = words;

	return text;	
}

void free_text(Text* text)
{
	int i;
	for(i=0;i<text->size;i++)
	{
		free((text->input)[i]);
	}
	free(text->input);
	free(text);
}
