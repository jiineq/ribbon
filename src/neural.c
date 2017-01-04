#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include "matrix.h"

float sigmoid(float x)
{
	return 1.0/(1.0 + exp(-x));
}

float ddxsigmoid(float x)
{
	return sigmoid(x) * (1 - sigmoid(x));
}

void read_weight(Matrix* m, char* filename)
{
	FILE* file = fopen(filename, "r");
	if(file == NULL)
	{
		printf("Cannot open file %s\n", filename);
		exit(0);
	}
	char* input = NULL;
	char buff[512];
	int size = 512;
	while(fgets(buff,512,file)!=NULL)
	{
		input = realloc(input, size);
		strcat(input, buff);
		size += 512;
	}

	char* item = strtok(input, ",");
	int i=0;
	while(item != NULL)
	{
		matrix_set(m, i/m->num_rows, i%m->num_cols, atof(item));
		item = strtok(NULL, ",");
		i++;
	}
	free(input);
}
