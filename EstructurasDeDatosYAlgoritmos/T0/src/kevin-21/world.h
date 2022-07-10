#ifndef SRC_WORLD_H_
#define SRC_WORLD_H_

#include "person.h"

typedef struct _world
{
	int n_countries;			//Numero de paises
	int *n_regions_countries;	//Numero de regiones por cada [pais]
	Person ***countries;		//Raiz del arbol de las personas por cada [pais][region]
	int **people_count;			//Numero de personas de cada [pais][region]
} World;

World* create_world(int countries);
void create_region(World *world, int idx, int amount);
Person* add_contact(World *world, Person* person, int id);


#endif
