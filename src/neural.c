#include <stdlib.h>
#include <stdio.h>
#include <math.h>

float sigmoid(float x)
{
	return 1.0/(1.0 + exp(-x));
}

float ddxsigmoid(float x)
{
	return sigmoid(x) * (1 - sigmoid(x));
}


