#include "node.h"
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>


struct output
{
	int* vecindario; //Array con vecindario rodeado de -1
    int* array; //Array general
    int* indexes; //Indexes de los pixeles correspondientes 
	int cantidad; // Cantidad de pixeles
};
typedef struct output Output;

bool quedan_pixeles(Output* output, int amount)
{
    for (int i=0; i<amount; i++)
    {
        if (output->array[i] != -1)
        {
            return true;
        }
    }
    return false;
}

Node* create_node(Node *parent)
{
	Node *new = (Node*)malloc(sizeof(Node));

	new->head = NULL;
    new->gray = NULL;
    new->tail = NULL;
    new->next = NULL;
    //new->prev = NULL;

	if (parent->head == NULL)
    {
        parent->head = new;
        parent->tail = new;
    }
    else
    {
        //new->prev = parent->tail;
        parent->tail->next = new;
        parent->tail = new;
    }

	return new;
}




/*
Al usar armar_vecindario
Usar el array para todos los hijos y despues liberar
int* array = malloc(img->amount * sizeof(int));
armar_vecindario(array,...)
¿Hay que armar autmaticamente los hijos del nodo con el array modificado?
int* copia_array = realloc(array, sizeof(array))
free(array)
*/

int* armar_vecindario(int index, int gray, int heigth, int width, int amount, Output* output, Node* parent) 
//Devuelve struct con el vecindario que comienza en index, rodeado de -1 y con la cantidad de pixeles
{
    // Hay que hacer que vecindario sea con puros -1 y despues llenarlo
    int vecino_1 = index - 1; //izquierda
    int vecino_2 = index + 1; //derecha
    int vecino_3 = index + width; //abajo
    int vecino_4 = index - width; //arriba

    output->vecindario[index] = output->array[index];
    if (output->array[index] == gray);
    {
        output->indexes[output->cantidad] = index;
        output->cantidad++;   
    }
    output->array[index] = -1; // Borra todo el vecindario

    if (vecino_1 >= 0 && vecino_1 % width != 0) //Hay vecino a la izquierda
    {
        if (output->array[vecino_1] != -1) //Aun no se revisa
        {
            if (output->array[vecino_1] >= gray)
            {
                output = armar_vecindario(vecino_1, gray, heigth, width, amount, output, parent);
            } 
        }
    }
    if ((vecino_2 -1) % width != 0 && vecino_2 < amount) //Hay vecino a la derecha
    {
        if (output->array[vecino_2] != -1) //Aun no se revisa
        {
            if (output->array[vecino_2] >= gray)
            {
                output = armar_vecindario(vecino_2, gray, heigth, width, amount, output, parent);
            } 
        }
    }
    if (vecino_3 < amount) //Hay vecino abajo
    {
        if (output->array[vecino_3] != -1) //Aun no se revisa
        {
            if (output->array[vecino_3] >= gray)
            {
                output = armar_vecindario(vecino_3, gray, heigth, width, amount, output, parent);
            } 
        }
    }
    if (vecino_4 >= 0) //Hay vecino arriba
    {
        if (output->array[vecino_4] != -1) //Aun no se revisa
        {
            if (output->array[vecino_4] >= gray)
            {
                output = armar_vecindario(vecino_4, gray, heigth, width, amount, output, parent);
            } 
        }
    }

    Node* nodo_nuevo = create_node(parent);
    nodo_nuevo->indexs;

    return output; // Lista con los indexes del vecindario
}

void continue_tree(int* array_continuacion, int amount, int minimo, int heigth, int width, Node* parent) //Uno por cada nivel de hijos?
{
    
    bool no_encontrado = true;
    bool fin = false;
    int color = minimo;
    int index_inicial = -1;
    int color_inicial = -1;
    int cantidad_color_correcto = 0;
    while (no_encontrado)
    {
        for (int i = 0; i < amount; i++)
        {
            if (array_continuacion[i] == color && no_encontrado) //Encontrar el color minimo
            {
                no_encontrado = false;
                index_inicial = i;
                color_inicial = array_continuacion[i];
            }
            else if (color > 127)
            {
                no_encontrado = false;
                fin = true;
            }
        }
        color++;
    }
    for (int i = 0; i < amount; i++)
    {
        if (array_continuacion[i] == color_inicial)
        {
            cantidad_color_correcto++;
        }
    }

    /* Tengo:
    - Color que sigue color_inicial
    - Cantidad de ese color cantidad_color_correcto
    - Index donde comienza index_inicial
    */
    if (fin == false) //Si no entra aqui, terminar (es una hoja)
    {
        int* copia_array = realloc(array_continuacion, sizeof(array_continuacion));
        int* vecindario = malloc(amount * sizeof(int));
        for (int i=0; i < amount; i++) //Armar vecindario lleno de -1
        {
            vecindario[i] = -1;
        }

        Output* output;
        output->vecindario = vecindario;
        output->cantidad = 0;
        output->array = array_continuacion;
        output = armar_vecindario(index_inicial, color_inicial, heigth, width, amount, output, parent);
        while (quedan_pixeles(output, amount))
        {
            output = armar_vecindario(index_inicial, color_inicial, heigth, width, amount, output, parent);
        }

        //Termina primer nodo y sus hijos
    }
}

Node* start_tree(int* array_inicial, int amount, int heigth, int width)
{
    Node *node_0 = (Node*)malloc(sizeof(Node));
    bool no_encontrado = true;
    int color = 0;
    int index_inicial = -1;
    int color_inicial = -1;
    int cantidad_color_correcto = 0;
    while (no_encontrado)
    {
        for (int i = 0; i < amount; i++) //Recorro los colores
        {
            if (array_inicial[i] == color && no_encontrado) //Encontrar el color minimo
            {
                no_encontrado = false;
                index_inicial = i;
                color_inicial = array_inicial[i];
            }
        }
        color++;
    }
    
    for (int i = 0; i < amount; i++)
    {
        if (array_inicial[i] == color_inicial) // Contar cantidad de indexes en nodo
        {
            cantidad_color_correcto++;
        }
    }

    
    node_0->gray = color_inicial;
    node_0->indexs = malloc(cantidad_color_correcto * sizeof(int));

    int index = 0;
    for (int i = 0; i < amount; i++)
    {
        if (array_inicial[i] == color_inicial)
        {
            node_0->indexs[index] = i; //Guardar indexes con color base
            index++;
            array_inicial[i] = -1; //Colores ya usados quedan como -1            
        }
    }

    continue_tree(array_inicial, amount, color_inicial, heigth, width, node_0);

    // Aqui ya filtré el primer nodo, y marque el color 0 con -1

    /*
    - Buscar vecinos proximo index
    - Si aun queda del mismo color, volver a aplicar
    - Cuando no queden, pasar a los hijos de el primer nodo
    - Cuando el vecinadrio sean puros -1 se termina
    */
    return node_0;
}