#include "queue_manager.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int cantidad_procesos_entrantes(Proceso** procesos, int time, int n_procesos){
    // función que en cada momento ve cuantos procesos deben entrar a la cola por primera vez
    int entrantes = 0;
    for (int i = 0; i < n_procesos; i++){
        if ((*procesos[i]).start_time == time){
            entrantes++;
        }
    }
    return entrantes;
};

Proceso** entry_process_to_system(Proceso** procesos, int time, int n_procesos) {
     // función que en cada momento del tiempo ingresa procesos a la cola por primera vez
     // esta función se debe llamar después de haber ingresado a la cola los procesos más prioritarios, como los que pasan a WAITING y los
     // que consumieron su quantum
     int cantidad_entrantes = cantidad_procesos_entrantes(procesos, time, n_procesos);
     int j = 0;
     Proceso** processes_to_entry = malloc(cantidad_entrantes*sizeof(Proceso));
     for (int i = 0; i < n_procesos; i++){
         if ((*procesos[i]).start_time == time){
            // processes_to_entry[j] = malloc(sizeof(Proceso));
            processes_to_entry[j] = procesos[i];
            j++;
        }
     }
     return processes_to_entry;

};

void swap(Proceso** xp, Proceso** yp)
{
    Proceso *temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
// Function to perform Selection Sort
void sort_procesos_entrantes(Proceso** arr, int n)
{
    int i, j, min_idx;
 
    // One by one move boundary of unsorted subarray
    for (i = 0; i < n-1 ; i++) {
 
        // Find the minimum element in unsorted array
        min_idx = i;
        for (j = i + 1; j < n; j++){
          if ((*arr[j]).fabric_number <= (*arr[min_idx]).fabric_number){
            if ((*arr[j]).fabric_number == (*arr[min_idx]).fabric_number){
              if(strcmp((*arr[j]).name,(*arr[min_idx]).name) < 0){
                min_idx = j;
              }
            }
            else {
              min_idx = j;
            }
            }
 
        // Swap the found minimum element
        // with the first element
        }
        swap(&arr[min_idx], &arr[i]);
        
    }
};

//TODO: función que desempate entre procesos nuevos