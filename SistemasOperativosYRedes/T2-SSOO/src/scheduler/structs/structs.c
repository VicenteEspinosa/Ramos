#include "stdio.h"
#include "structs.h"

Proceso* get_next_ready(Queue *queue)
{
    if (queue->head == NULL)
    {
        return NULL;
    }
    Proceso* actual = queue->head;
    while (actual->state != 1) // Definir estado en que es READY
    {
        actual = actual->next;
        if (actual == NULL)
        {
            return NULL;
        }
    }
    return actual;
}


void remove_from_queue(Queue *queue, Proceso *proceso)
{
    Proceso *next = proceso->next;
    Proceso *prev = proceso->prev;

    if (next != NULL) // No es utlimo
    {
        Proceso *next_process = next;

        if (prev != NULL) // Esta entre dos
        {
            Proceso *prev_process = prev;
            prev_process->next = next_process;
            next_process->prev = prev_process;
        }
        else // Es primero
        {
            next_process->prev = NULL;
            queue->head = next_process;
        }
    }
    else // Es ultimo
    {
        if (prev != NULL) // Hay más adelante
        {
            Proceso *prev_process = prev;
            prev->next = NULL;
            queue->tail = prev_process;
        }
        else // Está solo
        {
            queue->head = NULL;
            queue->tail = NULL;
        }
    }
    proceso->next = NULL;
    proceso->prev = NULL;
}


void insert_on_queue(Queue *queue, Proceso *proceso)
{
    if (queue->tail == NULL) //No hay nada en la fila
    {
        queue->head = proceso;
        queue->tail = proceso;
    }
    else
    {
        queue->tail->next = proceso;
        queue->tail = proceso;
    }
}

int get_quantum(Queue * queue, int fabric_number, int Q){
    // Se asume que hay al menos un proceso en cola
    // ni = Cantidad de procesos de la misma fabrica
    // f cantidad de fabricas con procesos
    int ni = 0, f=0;
    int f_1=0, f_2=0, f_3=0, f_4=0;
    
    Proceso *proceso = queue->head;
    while (proceso != NULL)
    {
        if (f_1 == 0 && proceso->fabric_number == 1)
        {
            f_1 = 1;
            f++;
        }
        if (f_2 == 0 && proceso->fabric_number == 2)
        {
            f_2 = 1;
            f++;
        }
        if (f_3 == 0 && proceso->fabric_number == 3)
        {
            f_3 = 1;
            f++;
        }
        if (f_4 == 0 && proceso->fabric_number == 4)
        {
            f_4 = 1;
            f++;
        }
        if (proceso->fabric_number == fabric_number)
        {
            ni++;
        }
        proceso = proceso->next;
    }
    return Q/(ni*f);
}