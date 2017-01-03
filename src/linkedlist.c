#include <stdlib.h>
#include <stdio.h>
#include "linkedlist.h"

void list_append(LinkedList* list, int data)
{
	if(list->tail==NULL)//if list->tail is null, then list->head should also be null, i.e. empty list
	{
		list->tail = malloc(sizeof(Node));
		if(list->tail==NULL)
		{
			printf("malloc failed\n");
			exit(1);
		}
		list->head = list->tail;

		(list->tail)->value = data;
		(list->tail)->next = NULL;
		(list->tail)->prev = NULL;
	}else
	{
		Node* temp = malloc(sizeof(Node));
		if(temp==NULL)
		{
			printf("malloc failed\n");
			exit(1);
		}
		temp->value = data;
		
		list->tail->next = temp;
		temp->prev = (list->tail);
		temp->next = NULL;
		(list->tail) = temp;
	}
}

void list_clear(LinkedList* list)
{
	Node* curr = list->head;
	while(curr!=NULL)
	{
		Node* temp = curr;
		curr = curr->next;
		free(temp);
	}
	list->head = NULL;
	list->tail = NULL;
}

void list_print(LinkedList* list)
{
	Node* temp = list->head;
	printf("[");
	while(temp!=NULL)
	{
		printf("%d,",temp->value);
		temp = temp->next;
	}
	printf("]\n");
}

