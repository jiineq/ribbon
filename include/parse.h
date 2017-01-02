#ifndef PARSE
#define PARSE

typedef struct Text
{
	char** input;
	int size;
} Text;

Text* parse_input(const char* filename);
void free_text(Text* text);

#endif

