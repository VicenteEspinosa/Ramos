#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "cpu_manager.h"
#include "../structs/structs.h"

int update_cpu_burst(Queue* cola, int quantum, int time) {
    Proceso* proceso = cola->in_cpu;
    if (quantum == 0){
        //se acabó el quantum
        proceso->interuptions ++;
        if (proceso->bursts[proceso->next_index] == 0){
        //se acabó el quantum y termino al mismo tiempo

            if (proceso->next_index < proceso->number_bursts-1){
                // no es la última ráfaga de cpu
                // proceso pasa a waiting, aumenta uno el next index y debe dejar la cpu e ir al final de la cola y reiniciar un quantum
                proceso->next_index ++;
                proceso->state = 2;
                insert_on_queue(cola, proceso);
                printf("[t = %d] El proceso %s ha pasado a WAITING\n", time, proceso->name);
                cola->in_cpu = NULL;

                return 1; //esto es para reiniciar el quantum


            }
            else {
                proceso->state = 3;
                printf("[t = %d] El proceso %s ha pasado a FINISHED\n", time, proceso->name);
                proceso->turnaround_time = time - proceso ->start_time;
                cola->in_cpu = NULL;
                return 2;
                //es la última ráfaga de cpu, por lo que proceso pasa a finished y sale del sistema
            }
        }
        proceso->state = 1;
        printf("[t = %d] El proceso %s fue interrumpido y ha pasado a READY\n", time, proceso->name);
        insert_on_queue(cola, proceso);
        cola->in_cpu = NULL;
        return 1;
    }
    else if (proceso->bursts[proceso->next_index] == 0){
        //se acabó la rafaga
        if (proceso->next_index < proceso->number_bursts-1){
            // no es la última ráfaga de cpu
            // proceso pasa a waiting, aumenta uno el next index y debe dejar la cpu e ir al final de la cola y reiniciar un quantum
            proceso->next_index ++;
            proceso->state = 2;
            insert_on_queue(cola, proceso);
            printf("[t = %d] El proceso %s ha pasado a WAITING\n", time, proceso->name);
            cola->in_cpu = NULL;

            return 1; //esto es para reiniciar el quantum


        }
        else {
            proceso->state = 3;
            printf("[t = %d] El proceso %s ha pasado a FINISHED\n", time, proceso->name);
            proceso->turnaround_time = time - proceso ->start_time;
            cola->in_cpu = NULL;
            return 2;
            //es la última ráfaga de cpu, por lo que proceso pasa a finished y sale del sistema
        }
    }
    else{
        //disminuye en uno la ráfaga
        proceso->bursts[proceso->next_index] --;
        return 0;
    }
};


void check_io_bursts(Queue* cola, int time){
    Proceso *proceso = cola->head;
    while (proceso != NULL)
    {
        if (proceso->state == 2){
            if(proceso->bursts[proceso->next_index] > 0){
                proceso->bursts[proceso->next_index] --;
            }
            else {
                proceso->state = 1;
                proceso->next_index ++;
                printf("[t = %d] El proceso %s ha pasado a READY\n", time, proceso->name);
            }
        }
        proceso -> waiting_time++;
        proceso = proceso->next;
    }
}