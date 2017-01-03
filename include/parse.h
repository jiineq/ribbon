#ifndef PARSE
#define PARSE
#include "linkedlist.h"
#define SYMBOLS "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
#define NUM_SYMBOLS 32

typedef struct Text
{
	char** input;
	LinkedList symbols[NUM_SYMBOLS]; //Each linkedlist is an array element which corresponds to a symbol, each pair of elements in the linkedlist corresponds to the index of the word in the text and the index of the chars in the word
	int size;
} Text;

//Creates Text struct from file
Text* parse_input(const char* filename);

//Reads a file and returns a malloced buffer of contents
char* read_file(const char* filename);

//frees Text struct
void free_text(Text* text);

//non-zero if a in the set !"#$%&'()*+,./:;<=>?@[\]^_`{|}~
int is_symbol(char a);

//index of first symbol if a contains a symbol defined as above
int contains_symbol(char* a);

//non-zero if a is nonprintable character
int is_nonprintable(char a);

//index of first nonprintable character
int contains_nonprintable(char* a);

//binary search through the symbol table
int symbol_bin_search(char key);

#endif

