#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "parse.h"

int main(int argc, char* argv[])
{
	if(argc < 2)
		printf("usage: ribbon input file..\n");
	else
	{
		printf("input file:%s\n", argv[1]);
		Text* text = parse_input(argv[1]);
		int i;
		for(i = 0; i<text->size; i++)
		{
			printf("%s ",(text->input)[i]);
		}
		free_text(text);
	}
	return 0;
}
