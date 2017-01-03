#ifndef LINKEDLIST_H
#define LINKEDLIST_H

typedef struct node
{
	int value;
	struct node* next;
	struct node* prev;
}Node;

typedef struct linkedlist
{
	Node* head;
	Node* tail;
}LinkedList;

void list_append(LinkedList* list, int value);
void list_clear(LinkedList* list);
void list_print(LinkedList* list);

#endif
