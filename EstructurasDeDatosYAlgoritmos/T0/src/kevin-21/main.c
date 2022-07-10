#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include "world.h"



/* Retorna true si ambos strings son iguales */
bool string_equals(char *string1, char *string2)
{
	return !strcmp(string1, string2);
}

/* Revisa que los parametros del programa sean validos */
bool check_arguments(int argc, char **argv)
{
	if (argc != 3)
	{
		printf("Modo de uso: %s INPUT OUTPUT\n", argv[0]);
		printf("Donde:\n");
		printf("\tINPUT es la ruta del archivo de input\n");
		printf("\tOUTPUT es la ruta del archivo de output\n");
		return false;
	}

	return true;
}

void print_espacios(int cantidad, FILE *output_file)
{
	for (int i = 0; i < cantidad; i++)
	{
		fprintf(output_file, "    ");	
	}
}

int main(int argc, char **argv)
{
//	World *world = create_world(2);
//	create_region(world,0,2);
//	create_region(world,1,5);
//	add_contact(world,world->countries[0][0],1);

	/* Si los parametros del programa son invalidos */
	if (!check_arguments(argc, argv))
	{
		/* Salimos del programa indicando que no termino correctamente */
		return 1;
	}

	/* Abrimos el archivo de input */
	FILE *input_file = fopen(argv[1], "r");

	/* Abrimos el archivo de output */
	FILE *output_file = fopen(argv[2], "w");


	char command[32];

	/* Leemos la cantidad de paises */
	int n_countries;
	fscanf(input_file, "%d", &n_countries);

	//TODO
	/* [Por implementar] Generamos nuestro mundo */
	World *world = create_world(n_countries);
	/* Leemos la cantidad de regiones de cada pais */
	int n_regions;
	for (int cty = 0; cty < n_countries; cty++)
	{
		fscanf(input_file, "%d", &n_regions);

		//TODO
		/* Poblamos el pais con regiones */
		create_region(world, cty, n_regions);
	}

	/* Numero de eventos/lineas */
	int n_lines;
	fscanf(input_file, "%d", &n_lines);

	/* Declaramos variables para guardar:
	- Id de pais.
	- Id de region.
	- Profundidad.
	- Id de contacto para las rutas
	- Numero de contactos.
	*/
	int country_id;
	int region_id;
	int depth;
	int contact_id;
	int n_contacts;


	while (n_lines)
	{
		/* Disminuimos en 1 el numero de lineas por leer */
		n_lines--;

		/* Leemos la instruccion */
		fscanf(input_file, "%s", command);

		/* Obtenemos pais, region, y profundidad */
		fscanf(input_file, "%d", &country_id);
		fscanf(input_file, "%d", &region_id);


		/* POSITIVE */
		if (string_equals(command, "ADD_CONTACTS"))
		{
			fscanf(input_file, "%d", &depth);
			/*printf("ADD_CONTACTS %d %d %d ", country_id, region_id, depth);*/

			/* Obtenemos la ruta desde el archivo*/
			Person *padre;
			padre = world->countries[country_id][region_id];
			for (int r = 0; r < depth; r++)
			{
				fscanf(input_file, "%d", &contact_id);
				padre = search_contact(padre, contact_id);
				/*printf("%d ", contact_id);*/
			}
			/* Obtenemos el numero de contactos */

			fscanf(input_file, "%d", &n_contacts);
			/*printf("%d\n", n_contacts);*/
			int estados;
			if (padre->state == 2)
				{estados = 1;}
			else
				{estados = 0;};

			for (int i = 0; i < n_contacts; i++)
			{
				create_person(padre, estados, world->people_count[country_id][region_id]);
				world->people_count[country_id][region_id]++;
			}
		}
		else if (string_equals(command, "POSITIVE"))
		{
			fscanf(input_file, "%d", &depth);
			/*printf("POSITIVE %d %d %d ", country_id, region_id, depth);*/
			Person *padre;
			padre = world->countries[country_id][region_id];
			/* Obtenemos la ruta desde el archivo*/
			for (int r = 0; r < depth; r++)
			{
				fscanf(input_file, "%d", &contact_id);
				padre = search_contact(padre, contact_id);
				/*printf("%d ", contact_id);*/
			}
			padre->state = 2;
			change_state_childs(padre, 1);
			/*printf("\n");*/
		}
		else if (string_equals(command, "NEGATIVE"))
		{
			fscanf(input_file, "%d", &depth);
			/*printf("NEGATIVE %d %d %d ", country_id, region_id, depth);*/
			Person *padre;
			padre = world->countries[country_id][region_id];
			/* Obtenemos la ruta desde el archivo*/
			for (int r = 0; r < depth; r++)
			{
				fscanf(input_file, "%d", &contact_id);
				padre = search_contact(padre, contact_id);
				/*printf("%d ", contact_id);*/
			}
			/*printf("\n");*/
			destroy_tree(padre, padre->id);
		}
		else if (string_equals(command, "RECOVERED"))
		{
			fscanf(input_file, "%d", &depth);
			/*printf("RECOVERED %d %d %d ", country_id, region_id, depth);*/
			Person *padre;
			padre = world->countries[country_id][region_id];
			/* Obtenemos la ruta desde el archivo*/
			for (int r = 0; r < depth; r++)
			{
				fscanf(input_file, "%d", &contact_id);
				padre = search_contact(padre, contact_id);
				/*printf("%d ", contact_id);*/
			}
			/*printf("\n");*/
			padre->state = 3;

			/* [Por implementar] */
		}
		else if (string_equals(command, "CORRECT"))
		{
			fscanf(input_file, "%d", &depth);
			/*printf("CORRECT %d %d %d ", country_id, region_id, depth);*/
			/* Obtenemos la primera ruta desde el archivo*/
			Person *persona1;
			persona1 = world->countries[country_id][region_id];
			Person *persona2;
			persona2 = world->countries[country_id][region_id];

			for (int r = 0; r < depth; r++)
			{
				fscanf(input_file, "%d", &contact_id);
				persona1 = search_contact(persona1, contact_id);
				/*printf("%d ", contact_id);*/
			}
			/* Obtenemos la segunda ruta desde el archivo*/
			fscanf(input_file, "%d", &depth);
			/*printf("%d ", depth);*/
			for (int r = 0; r < depth; r++)
			{
				fscanf(input_file, "%d", &contact_id);
				persona2 = search_contact(persona2, contact_id);
				/*printf("%d ", contact_id);*/
			}
			/*printf("\n");*/

			Person *head1;
			Person *tail1;

			head1 = persona1->head;
			tail1 = persona1->tail;

			if (head1 != NULL)
			{
				Person *actual;
				actual = head1;
				actual->parent = persona2;
				while (actual->next != NULL)
				{
					actual = actual->next;
					actual->parent = persona2;
				};
			};

			if (persona2->head != NULL)
			{
				Person *actual;
				actual = persona2->head;
				actual->parent = persona1;
				while (actual->next != NULL)
				{
					actual = actual->next;
					actual->parent = persona1;
				};
			};

			persona1->head = persona2->head;
			persona1->tail = persona2->tail;
			/*persona1->next = persona2->next;
			persona1->prev = persona2->prev;
			persona1->parent = persona2->parent;*/

			persona2->head = head1;
			persona2->tail = tail1;
			/*persona2->next = next1;
			persona2->prev = prev1;
			persona2->parent = padre1;*/

			if (persona1->state == 2)
			{
				change_state_childs(persona1, 1);
			};
			if (persona2->state == 2)
			{
				change_state_childs(persona2, 1);
			};
		}
		else if (string_equals(command, "INFORM"))
		{
			Person *persona;
			persona = world->countries[country_id][region_id];
			int depth;
			depth = 0;

			fprintf(output_file, "INFORM %d %d\n", country_id, region_id);
			fprintf(output_file, "%d:%d\n", persona->id, persona->state);

			if (persona->head != NULL)
			{
				depth++;
				persona = persona->head;
				print_espacios(depth, output_file);
				fprintf(output_file, "%d:%d\n", persona->id, persona->state);	
			}

			int helper;
			helper = 0;
			while(depth > 0)
			{
				while(persona->head != NULL)
				{
					persona = persona->head;
					depth++;
					print_espacios(depth, output_file);
					fprintf(output_file, "%d:%d\n", persona->id, persona->state);
				}
			
				if (persona->next != NULL)
				{
					persona = persona->next;
					print_espacios(depth, output_file);
					fprintf(output_file, "%d:%d\n", persona->id, persona->state);
				}
				else
				{
					if (persona->parent->next != NULL)
					{
						persona = persona->parent->next;
						depth--;
						print_espacios(depth, output_file);
						fprintf(output_file, "%d:%d\n", persona->id, persona->state);
					}
					else
					{
						while (depth > 0 && helper == 0)
						{
							persona = persona->parent;
							depth--;
							if (depth != 0)
							{
								if (persona->parent->next != NULL)
								{
									helper = 1;
									persona = persona->parent->next;
									depth--;
									print_espacios(depth, output_file);
									fprintf(output_file, "%d:%d\n", persona->id, persona->state);
								}
							}
						}
						helper = 0;
					}
				}
			}
		}


		else if (string_equals(command, "STATISTICS"))
		{
			//TODO
			fprintf(output_file, "STATISTICS %d %d\n", country_id, region_id);

			int depth;
			depth = 0;
			int sosepchosos; //0
			sosepchosos = 0;
			int sosepchosos_espera; //1
			sosepchosos_espera = 0;
			int contagiados; //2
			contagiados = 0;
			int recuperados; //3
			recuperados = 0;


			
			Person *persona;
			persona = world->countries[country_id][region_id];
			depth = 0;

			if (persona->state == 0) {sosepchosos++;}
			else if (persona->state == 1) {sosepchosos_espera++;}
			else if (persona->state == 2) {contagiados++;}
			else if (persona->state == 3) {recuperados++;}

			if (persona->head != NULL)
			{
				depth++;
				persona = persona->head;
				if (persona->state == 0) {sosepchosos++;}
				else if (persona->state == 1) {sosepchosos_espera++;}
				else if (persona->state == 2) {contagiados++;}
				else if (persona->state == 3) {recuperados++;}	
			}

			int helper;
			helper = 0;
			while(depth > 0)
			{
				while(persona->head != NULL)
				{
					persona = persona->head;
					depth++;
					if (persona->state == 0) {sosepchosos++;}
					else if (persona->state == 1) {sosepchosos_espera++;}
					else if (persona->state == 2) {contagiados++;}
					else if (persona->state == 3) {recuperados++;}
				}
			
				if (persona->next != NULL)
				{
					persona = persona->next;
					if (persona->state == 0) {sosepchosos++;}
					else if (persona->state == 1) {sosepchosos_espera++;}
					else if (persona->state == 2) {contagiados++;}
					else if (persona->state == 3) {recuperados++;}
				}
				else
				{
					if (persona->parent->next != NULL)
					{
						persona = persona->parent->next;
						depth--;
						if (persona->state == 0) {sosepchosos++;}
						else if (persona->state == 1) {sosepchosos_espera++;}
						else if (persona->state == 2) {contagiados++;}
						else if (persona->state == 3) {recuperados++;}
					}
					else
					{
						while (depth > 0 && helper == 0)
						{
							persona = persona->parent;
							depth--;
							if (depth != 0)
							{
								if (persona->parent->next != NULL)
								{
									helper = 1;
									persona = persona->parent->next;
									depth--;
									if (persona->state == 0) {sosepchosos++;}
									else if (persona->state == 1) {sosepchosos_espera++;}
									else if (persona->state == 2) {contagiados++;}
									else if (persona->state == 3) {recuperados++;}
								}
							}
						}
						helper = 0;
					}
				}
			}






		fprintf(output_file, "0:%d\n", sosepchosos);
		fprintf(output_file, "1:%d\n", sosepchosos_espera);
		fprintf(output_file, "2:%d\n", contagiados);
		fprintf(output_file, "3:%d\n", recuperados);
		}
	}

	/*  [Por implementar] Liberamos nuestra estructura */
	for (int cty = 0; cty < world->n_countries; cty++)
	{
		for (int reg = 0; reg < world->n_regions_countries[cty]; reg++)
		{
			Person *caso_0;
			caso_0 = world->countries[cty][reg];
			destroy_tree(caso_0, caso_0->id);
		}
		/* free(world->n_regions_countries[cty]); */
		free(world->countries[cty]);
		free(world->people_count[cty]);
	}
	free(world->countries);
	free(world->people_count);
	/*free(world->n_countries);*/
	free(world->n_regions_countries);
	free(world);

	fclose(input_file);
	fclose(output_file);
	return 0;
}
