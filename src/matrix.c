#include <stdlib.h>
#include <stdio.h>

#include "matrix.h"

Matrix* matrix_create(int num_rows, int num_cols)//zero matrix
{
	Matrix* m = malloc(sizeof(Matrix));
	m->num_rows = num_rows;
	m->num_cols = num_cols;

	m->rows = malloc(num_rows * sizeof(float*));
	m->values = calloc(num_rows * num_cols, sizeof(float));
	
	int i;
	for(i=0;i<num_rows;i++)
	{
		m->rows[i] = m->values + i * num_cols;
	}
	
	return m;
}

void matrix_free(Matrix* m)
{
	free(m->rows);
	free(m->values);
	free(m);
}

float matrix_get(Matrix* m, int r, int c)
{
	return (m->rows)[r][c];
}

void matrix_set(Matrix* m, int r, int c, float x)
{
	(m->rows)[r][c] = x;
}

Matrix* create_eye(int dim)
{
	Matrix* m = matrix_create(dim, dim);
	int i;
	for(i=0;i<dim;i++)
		matrix_set(m, i, i, 1);
	return m;
}

Matrix* matrix_add(Matrix* a, Matrix* b)
{
	if( a->num_rows == b->num_rows && a->num_cols == b->num_cols)
	{
		int i,j;
		for(i=0;i<a->num_rows;i++)
		{
			for(j=0;j<a->num_cols;j++)
			{
				float sum = matrix_get(a,i,j) + matrix_get(b,i,j);
				matrix_set(a, i, j, sum); 
			}
		}
		return a;
	}else
	{
		
		printf("Invalid Dims in addition of %x & %x\n",a,b);
		return NULL;
	}
}

Matrix* matrix_scalar(Matrix* a, float (*func)(float))
{
	int i,j;
	for(i=0;i<a->num_rows;i++)
	{
		for(j=0;j<a->num_cols;j++)
		{
			matrix_set(a, i, j, (func)(matrix_get(a,i,j)));
		}
	}
	return a;
}

Matrix* matrix_scalar_multiply(Matrix* a, float c)
{
	int i,j;
	for(i=0;i<a->num_rows;i++)
	{
		for(j=0;j<a->num_cols;j++)
		{
			matrix_set(a, i, j, matrix_get(a,i,j)*c);
		}
	}
	return a;
}

Matrix* matrix_multiply(Matrix* a, Matrix* b)
{
	if(a->num_cols == b->num_rows)
	{
		Matrix* m = matrix_create(a->num_rows, b->num_cols);
		int i,j,k;
		for(i = 0; i < m->num_rows; i++)
		{
			for(j = 0; j< m->num_cols; j++)
			{
				float sum = 0;
				for(k = 0; k < a->num_cols; k++)
				{
					sum += matrix_get(a,i,k) * matrix_get(b,k,j);
				}
				matrix_set(m,i,j,sum);
			}
		}
		return m;
	}else
	{
		printf("Invalid Dims in multipication of %x & %x\n",a,b);
		return NULL;
	}
}

Matrix* matrix_extend_rows(Matrix* m, int new_row_size)
{
	m->rows = realloc(m->rows, new_row_size * sizeof(float*));

	m->values = realloc(m->values, m->num_cols * new_row_size * sizeof(float));
	
	int diff = new_row_size - m->num_rows;
	int i, j;
	for(i=0;i<m->num_rows;i++)
	{
		m->rows[i] = m->values + i * m->num_cols;
	}

	for(i=m->num_rows;i<new_row_size;i++)
	{
		m->rows[i] = m->values + i * m->num_cols;
		for(j = 0; j < m->num_cols; j++)
		{
			matrix_set(m, i, j, matrix_get(m, i-m->num_rows, j));
		}
	}
	m->num_rows = new_row_size;
	return m;
}

//Square Matricies only
Matrix* matrix_sq_transpose(Matrix* m)
{
	int a,b;
	for(a = 0; a < m->num_rows-1; a++)
	{
		for(b = a+1; b < m->num_rows; b++)
		{
			float temp = matrix_get(m, a, b);
			matrix_set(m, a, b, matrix_get(m, b, a));
			matrix_set(m, b, a, temp);
		}
	}
}

void matrix_print(Matrix* a)
{
	int i,j;
	for(i=0;i<a->num_rows;i++)
	{
		printf("|");
		for(j=0;j<a->num_cols;j++)
		{
			printf("%.2f  ", matrix_get(a, i, j));
		}
		printf("|\n");
	}
	printf("\n");
}
/* debug purposes
int main()
{
	Matrix* a = matrix_create(2,4);
	
	Matrix* b = matrix_create(4,1);

	matrix_set(a, 0, 0, 22);
	matrix_set(a, 0, 1, 64);
	matrix_set(a, 1, 0, 32);
	matrix_set(a, 1, 3, 654);

	matrix_set(b, 3, 0, 5.22);
	matrix_set(b, 0, 0, 12);
	matrix_set(b, 2, 0, 7.231);
	matrix_set(b, 1, 0, -876.23);
	matrix_print(a);
	matrix_print(b);
	matrix_print(matrix_multiply(a,b));
	return 0;
}*/
