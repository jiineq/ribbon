#ifndef PARSE
#define PARSE
#define SYMBOLS "!\"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~"
#define NUM_SYMBOLS 31

typedef struct Text
{
	char** input;
	
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

#endif

