#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include "structs/structs.h"
#include "../file_manager/manager.h"
#include "queue_manager/queue_manager.h"
#include "cpu_manager/cpu_manager.h"



int quantum;
char* output_file_name;

void write_output(Proceso** procesos, int n_procesos){
  FILE *output_file = fopen(output_file_name, "w");
  for (int i = 0; i < n_procesos; i++){
    fprintf(output_file, "%s,", procesos[i]->name);
    fprintf(output_file, "%d,", procesos[i]->cpu_turns);
    fprintf(output_file, "%d,", procesos[i]->interuptions);
    fprintf(output_file, "%d,", procesos[i]->turnaround_time);
    fprintf(output_file, "%d,", procesos[i]->response_time);
    fprintf(output_file, "%d\n", procesos[i]->waiting_time);
    free(procesos[i]->bursts);
    free(procesos[i]);
  }
  fclose(output_file);
  free(procesos);
}

int main(int argc, char **argv) // Falta leer input y output
{
  int Q = 100;
  if (argc == 4){
    Q = atoi(argv[3]);
  }
  else if (argc < 3){
    printf("Modo de uso es: /scheduler <input> <output> <Q>\n");
    exit(0);
  }
  char* input_file_name = argv[1];
  output_file_name = argv[2];

  InputFile *file = read_file(input_file_name);


  int n_procesos = file->len;

  Proceso** procesos = malloc(file->len * sizeof(Proceso*));  //pedimos memoria para arreglo de procesos
  for (int i = 0; i < file->len; i++)
  {
    procesos[i] = malloc(sizeof(Proceso));

    char **line = file->lines[i];

    *procesos[i] = (Proceso){
      .prev = NULL,
      .next = NULL,
      .name = line[0],
      .start_time = atoi(line[1]),
      .fabric_number = atoi(line[2]),
      .pid = i,
      .next_index = 0,
      .state = 1,
      .number_bursts = atoi(line[3]) + atoi(line[3]) - 1,
      .bursts = malloc((atoi(line[3]) + atoi(line[3]) - 1)*sizeof(int)), //en line 3 viene la cantidad de ráfagas.
      .cpu_turns = 0,
      .interuptions = 0,
      .turnaround_time = 0,
      .response_time = -1,
      .waiting_time = 0,
    };
    for (int j=0; j<(*procesos[i]).number_bursts;j++){
      (*procesos[i]).bursts[j] = atoi(line[j+4]);
    }
  }

  int procesos_terminados = 0;
  int reiniciar_quantum;
  Queue* cola = malloc(sizeof(Queue));
  *cola = (Queue){
    .head = NULL,
    .tail = NULL,
    .in_cpu = NULL
  };
  
  for(int time=0; ; time++){
    int n_entrantes = cantidad_procesos_entrantes(procesos, time, file->len);

    Proceso** entrantes = entry_process_to_system(procesos, time, n_procesos);
    if (n_entrantes > 1){
      // si al mismo tiempo quieren entrar más de uno al sistema
      sort_procesos_entrantes(entrantes, n_entrantes);
    }
    for(int i=0; i<n_entrantes; i++){
      printf("[t = %d] El proceso %s ha sido creado\n", time, (*entrantes[i]).name);
    }
    if(cola->in_cpu != NULL){
      //acá entra cuando CPU está ocupada
      reiniciar_quantum = update_cpu_burst(cola, quantum, time);
      if(reiniciar_quantum == 0){
        quantum --;
      }
      else if (reiniciar_quantum == 2){
        procesos_terminados++;
        if(procesos_terminados == n_procesos){
          write_output(procesos, n_procesos);
          free(cola);
          free(entrantes);
          input_file_destroy(file);
          exit(0);
        }
      }
    }
    if (n_entrantes > 0){
      //si hay procesos que les toque entrar
      for(int i=0; i<n_entrantes; i++){
        insert_on_queue(cola, entrantes[i]);
      } 
    }
    if(cola->in_cpu == NULL){
      Proceso * proceso_ready = get_next_ready(cola);
      if(proceso_ready != NULL){
        printf("[t = %d] El proceso %s ha entrado a la CPU\n", time, proceso_ready->name);

        //lo removemos de la cola
        quantum = get_quantum(cola, proceso_ready->fabric_number, Q);
        remove_from_queue(cola, proceso_ready);
        cola->in_cpu = proceso_ready;
        proceso_ready->cpu_turns++;
        if(proceso_ready->response_time == -1){
          proceso_ready->response_time = time - proceso_ready->start_time;
        }
        proceso_ready->state = 0;
      }
      else
      {
        printf("[t = %d] La CPU esta vacía\n", time);
      }
    }
    check_io_bursts(cola, time);
    free(entrantes);
  }
  
}