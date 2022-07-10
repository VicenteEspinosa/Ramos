#include "../structs/structs.h"

int cantidad_procesos_entrantes(Proceso** procesos, int time, int n_procesos);

Proceso** entry_process_to_system(Proceso** procesos, int time, int n_procesos);

void swap(Proceso** xp, Proceso** yp);

void sort_procesos_entrantes(Proceso** arr, int n);

