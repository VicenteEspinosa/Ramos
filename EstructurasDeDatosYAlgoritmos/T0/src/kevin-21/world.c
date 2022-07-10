#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "world.h"

World* create_world(int countries)
{
	World *new = (World*)malloc(sizeof(World));
	memset(new,0,sizeof(World));
	new->n_countries = countries;
	new->n_regions_countries = (int*)malloc(sizeof(int)*countries);
	memset(new->n_regions_countries,0,sizeof(int)*countries);
	new->countries = (Person***)malloc((sizeof(Person***))*countries);
	memset(new->countries,0,(sizeof(Person***))*countries);
	new->people_count = (int**)malloc((sizeof(int**))*countries);
	memset(new->people_count,0,(sizeof(int**))*countries);

	return new;
}

void create_region(World *world, int idx, int amount)
{
	world->n_regions_countries[idx] = amount;
	world->countries[idx] = (Person**)malloc(sizeof(Person***)*amount);
	memset(world->countries[idx],0,sizeof(Person***)*amount);
	world->people_count[idx] = (int*)malloc(sizeof(int**)*amount);
	memset(world->people_count[idx],0,sizeof(int**)*amount);

	for (int i=0; i<amount; i++)
	{
		world->countries[idx][i] = create_person(NULL,2,0);
		world->people_count[idx][i]++;
	}
}

Person* add_contact(World *world, Person* person, int id)
{
	Person* new = NULL;
	if (person->state==2)
		new = create_person(person,id,1);
	else
		new = create_person(person,id,0);

	return new;
}
