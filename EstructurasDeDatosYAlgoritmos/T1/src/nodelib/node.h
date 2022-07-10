typedef struct _node
{
	int gray; //Color del nodo
	int amount; //CAntidad de pixeles
	int* indexs; //Indexes de los pixeles
/*
	int* grays;
	int* grays_vecinos;
	int* indexs_vecinos;
*/

	struct _node *head;
	struct _node *tail;
	struct _node *next;
	//struct _node *prev;

} Node;

Node* start_tree(int* array_inicial, int amount, int heigth, int width);

/*
Person* search_contact(Person *person, int idx);
Person* destroy_tree(Person *person, int id_inicial);
Person* change_state_childs(Person *person, int state);
*/