#ifndef MATRIX_H
#define MATRIX_H

typedef struct Matrix
{
	float** rows;
	float* values;
	int num_rows;
	int num_cols;

} Matrix;

//Creates zero matrix
Matrix* matrix_create(int num_rows, int num_cols);

//frees matrix
void matrix_free(Matrix* m);

//returns an entry in the matrix
float matrix_get(Matrix* m, int r, int c);

//changes an entry in the matrix
void matrix_set(Matrix* m, int r, int c, float x);

//creates identity matrix
Matrix* create_eye(int dim);

//Adds matrix a and b and stores the result back into a and returns a
Matrix* matrix_add(Matrix* a, Matrix* b);

//Applies function func on each entry in the matrix and returns the matrix
Matrix* matrix_scalar(Matrix* m, float (*func)(float));

//Scalar multiplication, returns the matrix
Matrix* matrix_scalar_multiply(Matrix* m, float c);

//multiplies matrices a and b, i.e a*b. returns a new matrix of the result
//Must free returned matrix
Matrix* matrix_multiply(Matrix* a, Matrix* b);

//Duplicates additional rows into m
Matrix* matrix_extend_rows(Matrix* m, int new_row_size);

//transposes m, m must be square
Matrix* matrix_sq_transpose(Matrix* m);

//prints the content of matrix to stdout
void matrix_print(Matrix* m);

#endif
