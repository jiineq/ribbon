#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "parse.h"

Text* parse_input(const char* filename)
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

	//Reads into buffer by words
	char** words = NULL;
	words = malloc(sizeof(char*)*512); //mem for 512 words
	size = 0;
	char* word = strtok(input, " ");
	while(word != NULL)
	{
		words[size] = malloc(strlen(word)+1); //mem for the word\0
		strcpy(words[size], word);
		size++;
		if(size%512==0)
		{
			words = realloc(words, size+512);
		}
		word = strtok(NULL, " ");
	}
	free(input);

	Text* text = malloc(sizeof(Text));
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
