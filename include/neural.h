#ifndef NEURAL_H
#define NERUAL_H

#define NUM_LAYERS 8

float sigmoid(float x);
float ddxsigmoid(float x);

//Reads the weight represented in the file to a matrix
void read_weight(Matrix* m, char* filename);


#endif
