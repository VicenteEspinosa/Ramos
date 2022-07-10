#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "person.h"

Person* create_person(Person *parent, int state, int id)
{
	Person *new = (Person*)malloc(sizeof(Person));
	memset(new,0,sizeof(Person));
	new->id = id;
	new->state = state;
	new->parent = parent;

	if (parent!=NULL)
	{
		if (parent->head!=NULL)
		{
			new->prev = parent->tail;
			parent->tail->next = new;
			parent->tail = new;
		}
		else
		{
			parent->head = new;
			parent->tail = new;
		}
	}

	return new;
}

Person* search_contact(Person *person, int idx)
{
	if (person->head == NULL)
		return NULL;

	Person* p = person->head;
	while (p!=NULL)
	{
		if (p->id==idx)
			return p;
		else p = p->next;
	}
	return NULL;
}

Person* destroy_tree(Person *person, int id_inicial)
{
	if (person->head!= NULL)
	{
		Person *hijo;
		hijo = person->head;
		destroy_tree(hijo, id_inicial);
	}
	else
	{
		if (person->id != id_inicial)
		{
			if (person->next == NULL)
			{
				Person *padre;
				padre = person->parent;
				padre->head = NULL;
				free(person);
				destroy_tree(padre, id_inicial);
			}
			else
			{
				Person *derecha;
				derecha = person->next;
				free(person);
				destroy_tree(derecha, id_inicial);
			};
		}
		else
		{
			if (person->id != 0)
			{
				if (person->parent->head == person && person->parent->tail == person) //Unico hijo
				{
					person->parent->head = NULL;
					person->parent->tail = NULL;
				}
				else if (person->parent->head == person) //Primero
				{
					person->parent->head = person->next;
					person->next->prev = NULL;
				}
				else if (person->parent->tail == person) //Ultimo
				{
					person->parent->tail = person->prev;
					person->prev->next = NULL;
				}
				else //Al medio
				{
					person->next->prev = person->prev;
					person->prev->next = person->next;
				}
			}
			free(person);
		}
	}
	return NULL;
}

Person* change_state_childs(Person *person, int state)
{
	if (person->head!= NULL)
		{if (state == 1)
			{
				Person *hijo;
				hijo = person->head;
				if (hijo->state == 0)
				{
					hijo->state = 1;
				}
				while (hijo->next!=NULL)
				{
					hijo = hijo->next;
					if (hijo->state == 0)
					{
						hijo->state = 1;
					}
				}
			}
		else
			{
				Person *hijo;
				hijo = person->head;
				hijo->state = state;
				while (hijo->next!=NULL)
				{
					hijo = hijo->next;
					hijo->state = state;
				}
			}
		}
	return NULL;
}
