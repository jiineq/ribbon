#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "parse.h"
#include "matrix.h"
#include "neural.h"

int main(int argc, char* argv[])
{
	if(argc < 2)
	{
		printf("usage: ribbon input file..\n");
	/*	Matrix* m = matrix_create(5,5);
		read_weight(m, "./weights/weight0");
		matrix_print(m);
		matrix_free(m);*/
	}
	else
	{
		Text* text = parse_input(argv[1]);
		int i;
		for(i = 0; i<text->size; i++)
		{
			printf("%s ",(text->input)[i]);
		}
		printf("\n");
		free_text(text);
	}
	return 0;
}
