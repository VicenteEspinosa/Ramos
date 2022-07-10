#include <stdio.h>
#include <stdlib.h>

typedef struct crmsFile
{
  char* name;
  char mode;
  int opened;
  u_int32_t address;
  int temp_bytes; //la cantidad de bytes que se llevan leidos o escritos
  u_int32_t size;
  unsigned char vpn;
  u_int32_t offset;
  int frame;
  int bytes_avanzados;
  int actual_process;
  int file_entrada;
} CrmsFile;

char* path;

// funciones generales
void cr_mount(char* memory_path);
void cr_ls_processes();
int cr_exists(int process_id, char* file_name);
void cr_ls_files(int process_id);

//funciones procesos
void cr_start_process(int process_id, char* process_name);
void cr_finish_process(int process_id);

//funciones archivos
CrmsFile* cr_open(int process_id, char* file_name, char mode);
int cr_write_file(CrmsFile* file_desc, void* buffer, int n_bytes);
int cr_read(CrmsFile* file_desc, void* buffer, int n_bytes);
void cr_delete_file(CrmsFile* file_desc);
void cr_close(CrmsFile* file_desc);
void print_process_files();