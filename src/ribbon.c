#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "parse.h"
#include "linkedlist.h"

int main(int argc, char* argv[])
{
	if(argc < 2)
		printf("usage: ribbon input file..\n");
	else
	{
		Text* text = parse_input(argv[1]);
		int i;
		for(i = 0; i<text->size; i++)
		{
			printf("%s ",(text->input)[i]);
		}
		printf("\n");
		const char* symbols = SYMBOLS;
		for(i=0;i<32;i++)
		{
			printf("%c: ", symbols[i]);
			list_print((text->symbols)+i);
		}
		printf("\n");
		free_text(text);
	}
	return 0;
}
