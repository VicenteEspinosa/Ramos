#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "crms_API.h"

FILE *fs;

int main(int argc, char *argv[])
{
  
  if (!argv[1]){
    printf("Debes ingresar el nombre del archivo con la memoria\n");
    return(0);
  }
  cr_mount(argv[1]);
  //cr_ls_files(0);
  //cr_ls_files(28);
 


  //cr_ls_processes();
  
  //char* file_name = "im_a_mp3.bin";
  //int process_id = 0;
  //if (cr_exists(process_id, file_name))
  //{
  //  printf("SI existe el archivo %s en el proceso de ID %d\n", file_name, process_id);
  //}
  //else
  //{
  //  printf("NO existe el archivo %s en el proceso de ID %d\n", file_name, process_id);
  //}
  //CrmsFile* file = cr_open(27, "prueba1.txt", 'w');
  //printf("VPN: %d\n",file->vpn);
  //int n_bytes = 9513795;
  //unsigned char* buffer = malloc(n_bytes*sizeof(unsigned char));
  //unsigned char buffer2[n_bytes];
  //cr_read(file, buffer, n_bytes);
  // printf("BUFFER: %s\n", buffer);
  //free(buffer);

  // print_process_files();
  //cr_delete_file(file);
  
  print_process_files();
 
  cr_close(file);
  

  // for(int x=0; x< n_bytes; x++){
  //   printf("buffer[%i] ->%i \n", x, buffer2[x]);
  //   fprintf(ff, "%c ", buffer2[x]);
  // }
  // fclose(ff);

  return(0);
}