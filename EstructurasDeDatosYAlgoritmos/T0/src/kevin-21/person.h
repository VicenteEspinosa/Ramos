#ifndef SRC_PERSON_H_
#define SRC_PERSON_H_

typedef struct _person
{
	int id;
	int state;

	struct _person *parent;
	struct _person *head;
	struct _person *tail;
	struct _person *prev;
	struct _person *next;
} Person;

Person* create_person(Person *parent, int state, int id);
Person* search_contact(Person *person, int idx);
Person* destroy_tree(Person *person, int id_inicial);
Person* change_state_childs(Person *person, int state);

#endif
