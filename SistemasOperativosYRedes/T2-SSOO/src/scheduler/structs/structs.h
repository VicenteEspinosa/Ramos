#ifndef STRUCTS_H
#define STRUCTS_H

typedef enum process_status
{
    RUNNING,
    READY,
    WAITING,
    FINISHED,
} STATUS;



typedef struct proceso
{
	int pid;
    int fabric_number;
	STATUS state;
    int number_bursts;
    int* bursts; //ráfagas. este arreglo comienza con cpu burst y también termina con cpu burst. después de cpu burst siempre viene i/o burst
    int next_index;
    int start_time;
    struct proceso *prev;
	struct proceso *next;

    char* name;
    int cpu_turns; //Numero de veces que entro a CPU
    int interuptions; //Numero de veces que no termino el burst
    int turnaround_time; //Tiempo desde que entró hasta que termina ultima rafaga
    int response_time; // El tiempo desde que el proceso llega al sistema hasta que pasa a RUNNING por primera vez.
    int waiting_time; //la suma de tiempo en ready y waiting, es decir, lo que demora en ser atendido

} Proceso;


typedef struct queue
{
    Proceso *head; //primero de la cola
    Proceso *tail; //último de la cola
    Proceso* in_cpu; //proceso que está en la cpu
} Queue;


Proceso* get_next_ready(Queue *queue);
void remove_from_queue(Queue *queue, Proceso *proceso);
void insert_on_queue(Queue *queue, Proceso *proceso);
int get_quantum(Queue * queue, int fabric_number, int Q);

#endif