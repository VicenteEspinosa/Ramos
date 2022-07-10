#include "crms_API.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <byteswap.h>

FILE *fp;

void cr_start_process(int process_id, char* process_name)
{
  int actual_process = 0;
  unsigned char buffer[256];
  int state = 1;
  int hay = 0;
  fp = fopen("memfilled.bin", "rb+");
  fseek(fp, 0, SEEK_SET);

  for (int i=0; i<16; i++)
  {
    fread(buffer, 8, 14, fp);
    if (!buffer[0])
    {
      fseek(fp, (actual_process * 256), SEEK_SET);
      fwrite(&state, 1, 1, fp);
      fseek(fp, (actual_process * 256) + 1, SEEK_SET);
      fwrite(&process_id, 1, 1, fp);
      fseek(fp, (actual_process * 256) + 2, SEEK_SET);
      fwrite(process_name, 12, 1, fp);
      printf("entrada: %d\n", actual_process);
      printf("Esta disponible\n");
      hay = 1;
      break;
    }
    actual_process++;
    fseek(fp, actual_process * 256, SEEK_SET);
  }
  fclose(fp);
  if (!hay)
  {
    printf("No hay espacio disponible en la tabla PCB\n");
  }
}

void cr_finish_process(int process_id)
{
  int actual_process = 0;
  int cero = 0;
  int bitmap_bit;
  int byte;
  int bit;
  int nuevo_byte;
  u_int32_t size;
  u_int32_t direction;
  u_int32_t offset;
  u_int32_t direccion_fisica;
  unsigned char vpn;
  unsigned char pfn;
  unsigned char virtual_direction[4];
  unsigned char buffer[256];
  unsigned char sub_buffer[21];
  unsigned char buffer_page_table[32];
  unsigned char buffer_bitmap[16];

  fp = fopen("memfilled.bin", "rb+");
  fseek(fp, 0, SEEK_SET);

  for (int i=0; i<16; i++)
  {
    fread(buffer, 8, 14, fp);
    if (buffer[1] == process_id && buffer[0])
    {
      for(int j = 0; j<10; j++)
      {
        fseek(fp, (actual_process * 256) + 14 + (21*j), SEEK_SET);
        fread(sub_buffer, 8, 21, fp);
        if (sub_buffer[0])
        {
          size = (sub_buffer[13] << 24) + (sub_buffer[14] << 16) + (sub_buffer[15] << 8) + sub_buffer[16];
          direction =   
          printf("Tiene archivo\n");
          printf("    - File con size %i y direccion virtual= %i \n", size, direction);
          for (int n=17; n<21; n++)
          {
            virtual_direction[n-17] = sub_buffer[n];
          }
          vpn = virtual_direction[0] << 1;
          if (virtual_direction[1] & (1 << 7))
          {
            vpn = vpn || (0x01 << 0);
          }
          printf("VPN: %d\n", vpn); 
          offset = ((virtual_direction[1] & (~(0x01 << 7))) << 16) + (virtual_direction[2] << 8) + virtual_direction[3];
          printf("offset: %d\n", offset);

          fseek(fp, actual_process*256 + 224, SEEK_SET);
          fread(buffer_page_table, 1, 32, fp);

          if((buffer_page_table[vpn] >> 7) & 0x01){ 
            printf("valor en tabla de pagina: %d\n", buffer_page_table[vpn]);
            pfn = buffer_page_table[vpn] & (~(0x01 << 7));
            printf("pfn: %d\n", pfn);
          }
          else {
            printf("entrada no válida");
          }
          direccion_fisica = (pfn << 23) + offset;
          printf("direccion fisica: %d\n", direccion_fisica);

          // Ahora invalidamos las entradas de los archivos del bitmap frame
          fseek(fp, 4*1024, SEEK_SET);
          byte = pfn/8;
          bit = 7 - (pfn - (byte*8));  // aca queda para leerlo de derecha a izquierda
          fread(buffer_bitmap, 1, 16, fp);
          nuevo_byte = ((buffer_bitmap[byte]) & (~(0x01 << bit)));
          fseek(fp, (4*1024) + byte, SEEK_SET);
          
          printf("byte en cuestion: %d, nuevo byte %d\n", buffer_bitmap[byte], nuevo_byte);
          printf("byte %d, bit %d\n", byte, bit);
          fwrite(&nuevo_byte, 1, 1, fp);
          fseek(fp, 4*1024, SEEK_SET);
          fread(buffer_bitmap, 1, 16, fp);
          printf("CAMBIADOOO %d\n", buffer_bitmap[byte]);
          
          //Ahora vamos invalidar la entrada en la tabla de paginas con el vpn
          fseek(fp, actual_process*256 + 224, SEEK_SET);
          fwrite(&cero, 1, 1, fp);

          // Invalidamos la entrada del archivo (byte = 0)
          fseek(fp, (actual_process * 256) + 14 + (21*j), SEEK_SET);
          fwrite(&cero, 1, 1, fp);

        }
      }
      //Invalidamos el proceso
      fseek(fp, (actual_process * 256), SEEK_SET);
      fwrite(&cero, 1, 1, fp);  
      break;
    }
    actual_process++;
    fseek(fp, actual_process * 256, SEEK_SET);
  }
  
  fclose(fp);
}





void cr_mount(char* memory_path){
  //monta variable global path
  path = memory_path;
}

void cr_ls_files(int process_id){
  //lista archivos del proceso
  FILE* fp;
  unsigned char buffer[256];
  unsigned char sub_buffer[21];
  int actual_process = 0;
  fp = fopen(path, "rb");
  int found=0;
  for(int x=0; x<16; x++){
    fseek(fp, actual_process * 256, SEEK_SET);
    fread(buffer,1, 256,fp);
    if (buffer[1] == process_id && buffer[0]){
      found=1;
      break;
    }
    actual_process++;
  }
  if(found){
    printf("Los siguientes son los archivos del proceso con ID: %i\n", process_id);
    int count_files = 0;
    for (int y=0; y<10; y++){
      fseek(fp, actual_process * 256 + 14 + 21*y, SEEK_SET);
      fread(sub_buffer, 1, 13, fp);
      if (sub_buffer[0]){
        count_files++;
        unsigned char name_file[13];
        for(int i = 1; i<13; i++)
        {
          name_file[i-1] = sub_buffer[i];
        }
        name_file[12] = '\0';
        printf("%s\n", name_file);

      }
    }
    if (!count_files){
      printf("El proceso con ID %i no tiene archivos\n", process_id);
    }
  } else {
    printf("No existe un proceso con ese ID en memoria\n");
  }
  fclose (fp);
}; 


void cr_ls_processes()
{
    /* Hay 16 entradas de 256B cada uno */

    int actual_process = 0;
    unsigned char buffer[256];
    unsigned char sub_buffer[21];
    fp = fopen(path, "rb");
    fseek(fp, 0, SEEK_SET);
    unsigned char name[13];
    int valid = 1;
    for(int i = 0; i<16; i++) /* Uno para cada proceso */
    {
        fread(buffer, 8, 14, fp);
        if (buffer[0])
        {
        

            for(int x = 2; x<14;x++) /* Uno para cada letra */
            {
                name[x-2] = buffer[x];
            }
            name[12] = '\0';
            printf("Proceso: %s  con id: %d  en ejecución, Entrada: %d \n", name, buffer[1], actual_process);
        }


        actual_process++;
        fseek(fp, actual_process * 256, SEEK_SET);
        
    }
    fclose(fp);
}

int cr_exists(int process_id, char* file_name)
{
    /* Hay 16 entradas de 256B cada uno */

    int actual_process = 0;
    unsigned char buffer[256];
    unsigned char sub_buffer[21];
    fp = fopen(path, "rb");
    fseek(fp, 0, SEEK_SET);
    unsigned char name[12];
    int valid = 1;
    for(int i = 0; i<16; i++) /* Uno para cada proceso */
    {
        fread(buffer, 8, 14, fp);
        if (buffer[1] == process_id)
        {
        
            /* Hay 10 archivos de 14B cada uno */

            for(int j = 0; j<10; j++)
            {
                fseek(fp, actual_process * 256 + 14 + 21*j, SEEK_SET);
                fread(sub_buffer, 8, 13, fp);
                if (sub_buffer[0])
                {
                    valid = 1;
                    for(int e = 1; e<13;e++) /* Uno para cada letra */
                    {
                        if (file_name[e-1] != sub_buffer[e])
                        {
                            valid = 0;
                            break;
                        }
                        name[e-1] = sub_buffer[e];
                    }
                    if (valid == 1)
                    {
                        fclose(fp);
                        return 1;
                    }
                }
            }
        }


        actual_process++;
        fseek(fp, actual_process * 256, SEEK_SET);
    }
    fclose(fp);
    return 0;
}

void print_process_files() /* Funcion para testear no mas */
{
    /* Hay 16 entradas de 256B cada uno */

    int actual_process = 0;
    unsigned char buffer[256];
    unsigned char sub_buffer[21];
    fp = fopen(path, "rb");
    fseek(fp, 0, SEEK_SET);
    unsigned char name[13];
    for(int i = 0; i<16; i++) /* Uno para cada proceso */
    {
        fread(buffer, 8, 14, fp);
        if (buffer[0])
        {
            for(int x = 2; x<14;x++) /* Uno para cada letra */
            {
                name[x-2] = buffer[x];
            }
            name[12] = '\0';
            printf("[Process: %s]  [Id: %d]  [Entrada: %d]\n", name, buffer[1], actual_process);
            
            /* Hay 10 archivos de 14B cada uno */

            for(int j = 0; j<10; j++)
            {
                fseek(fp, actual_process * 256 + 14 + 21*j, SEEK_SET);
                fread(sub_buffer, 8, 13, fp);
                if (sub_buffer[0])
                {
                    for(int e = 1; e<13;e++) /* Uno para cada letra */
                    {
                        name[e-1] = sub_buffer[e];
                    }
                    name[12] = '\0';
                    printf("    - File: %s\n", name);
                }
            }
        }



        actual_process++;
        fseek(fp, actual_process * 256, SEEK_SET);
    }

    fclose(fp);
}

CrmsFile* cr_open(int process_id, char* file_name, char mode)
{
  unsigned char buffer[14];
  unsigned char sub_buffer[21];
  unsigned char virtual_adress[4];
  unsigned char buffer_bitmap[16];
  unsigned char buffer_page_table[32];
  unsigned char vpn;
  int first_frame;
  unsigned char pfn;
  u_int32_t offset;
  u_int32_t file_size;
  u_int32_t vpn2;
  u_int32_t memoria_virtual;
  int uno= 1;
  int cero= 0;
  int adress;
  int valid;
  unsigned char name[12];
  CrmsFile *file = malloc(sizeof(CrmsFile));

  int actual_process = 0;
  fp = fopen(path, "rb+");
  fseek(fp, 0, SEEK_SET);
  for(int i = 0; i<16; i++) /* Uno para cada proceso */
  {
      fread(buffer, 1, 14, fp);
      if (buffer[1] == process_id && buffer[0])
      {
        for(int j = 0; j<10; j++)
        {
          fseek(fp, actual_process * 256 + 14 + 21*j, SEEK_SET);
          fread(sub_buffer, 1, 21, fp);
          if (sub_buffer[0])
          {
            valid = 1;
            for(int e = 1; e<13;e++) /* Uno para cada letra */
            {
                if (file_name[e-1] != sub_buffer[e])
                {
                    valid = 0;
                    break;
                }
                name[e-1] = sub_buffer[e];
            }
            if (valid == 1)
            {
              for (int x=17; x<21; x++)
              {
                virtual_adress[x-17] = sub_buffer[x];
              }
              // for (int x=0; x<4; x++)
              // {
              //   printf("Virtual adress: %u\n", virtual_adress[x]);
              // }
              file_size = (sub_buffer[13] << 24) + (sub_buffer[14] << 16) + (sub_buffer[15] << 8) + sub_buffer[16];

              u_int32_t myint = (virtual_adress[0] << 24) + (virtual_adress[1] << 16) + (virtual_adress[2] << 8) + virtual_adress[3];
              printf("Virtual Address: %d \n", myint);

              vpn = virtual_adress[0] << 1;
              if (virtual_adress[1] & (1 << 7)){
                vpn = vpn || (0x01 << 0);
              }
              printf("Virtual Page Number: %d\n", vpn);
              offset = ((virtual_adress[1] & (~(0x01 << 7))) << 16) + (virtual_adress[2] << 8) + virtual_adress[3];

              printf("Offset: %d\n", offset);
              

              fseek(fp, actual_process*256 + 224, SEEK_SET);
              fread(buffer_page_table, 1, 32, fp);

              if((buffer_page_table[vpn] >> 7) & 0x01){
                //printf("entrada es valida: %d\n", buffer_page_table[vpn]);
                pfn = buffer_page_table[vpn] & (~(0x01 << 7));
                printf("Page frame number: %d\n", pfn);
              }
              else {
                printf("entrada no válida\n");
                return(0);
              }

              u_int32_t direccion_fisica = (pfn << 23) + offset;

              printf("Direccion fisica: %d\n", direccion_fisica);
              printf("Tamaño archivo: %d\n", file_size);

              if (mode == 'r')
              {
                *file = (CrmsFile)
                {
                  .name = file_name,
                  .address = direccion_fisica,
                  .mode = mode,
                  .opened = 1,
                  .temp_bytes = 0,
                  .offset = offset,
                  .vpn = vpn,
                  .size = file_size,
                  .frame = 0,
                  .actual_process = actual_process,
                  .bytes_avanzados = 0,
                  .file_entrada = j
                };
                fclose(fp);
                return file;
              }
              return 0; //ERROR

            }
          }
        }
        if(mode == 'w'){
          fseek(fp, 4*1024, SEEK_SET); //frame bitmap
        fread(buffer_bitmap, 1, 16, fp);
        for (int i = 0; i<16; i++)
        {
          for (int x = 0; x<8; x++)
          {
            if (!((buffer_bitmap[i] >> x) & 0x01)) // Esta desocupado
            {
              first_frame = (4*1024) + 16 + (8*1024*1024 * (i * 8 + x));
              u_int32_t direccion_fisica = first_frame; // 30 bits significativos
              offset = direccion_fisica;
              for (int g = 23; g<30; g++)
              {
                offset = offset & (~(0x01  << g));
              }
              pfn = direccion_fisica >> 23;
              fseek(fp, actual_process * 256 + 10*21 + 14, SEEK_SET);
              fread(buffer_page_table, 1, 32, fp);
              for (int g = 0; g<32; g++)
              {
                if ((buffer_page_table[g] >> 7) & 0x01)
                {
                  if ((buffer_page_table[g] & (~(0x01 << 7))) == pfn)
                  {
                    vpn = g;
                  }
                }
              }
              memoria_virtual = (vpn<< 23) + offset;
              printf("Dirección virtual: %d\n", memoria_virtual);
              x = 10;
              i = 20;

              for(int j = 0; j<10; j++)
              {
                fseek(fp, actual_process * 256 + 14 + 21*j, SEEK_SET);
                fread(sub_buffer, 1, 14, fp);
                if (!sub_buffer[0])
                {
                  fseek(fp, actual_process * 256 + 14 + 21*j, SEEK_SET);
                  fwrite(&uno, 1, 1, fp);
                  fseek(fp, actual_process * 256 + 14 + 21*j + 1, SEEK_SET);

                  fwrite(file_name, 12, 1, fp);
                  fseek(fp, actual_process * 256 + 14 + 21*j + 13, SEEK_SET);

                  fwrite(&cero, 4, 1, fp);
                  fseek(fp, actual_process * 256 + 14 + 21*j + 17, SEEK_SET);
                  fwrite(&memoria_virtual, 4, 1, fp);
                  *file = (CrmsFile)
                  {
                    .name = file_name,
                    .address = direccion_fisica,
                    .mode = mode,
                    .opened = 1,
                    .temp_bytes = 0,
                    .vpn = vpn,
                    .offset = offset,
                    .size = 0,
                    .frame = 0,
                    .actual_process = actual_process,
                    .bytes_avanzados = 0,
                    .file_entrada = j
                  };
                  fclose(fp);
                  return file;
                }
              }
              printf("Proceso ya tiene 10 archivos.\n");             
             }
           }
        }
      }
      fclose(fp);
      return(0);
        // No encontro el archivo pero si el proceso
        
    }
      actual_process++;
      fseek(fp, actual_process * 256, SEEK_SET);
  }
  fclose(fp);

}

int cr_read(CrmsFile* file_desc, void* buffer, int n_bytes){
  unsigned char buffer_page_table[32];
  u_int32_t file_address = file_desc->address;
  u_int32_t bytes_a_leer;
  unsigned char pfn;
  unsigned char* temp_buffer = malloc(n_bytes*sizeof(unsigned char));
  int falto_por_leer = -1;
  u_int32_t queda_por_terminar_frame;
  int count_bytes = 0; 
  fp = fopen(path, "rb");

  if (file_desc->mode != 'r'){
    printf("Modo no está en r\n");
    free(temp_buffer);
    return -1;
  }
  fseek(fp, file_desc->actual_process*256 + 224, SEEK_SET);
  fread(buffer_page_table, 1, 32, fp);

  while(falto_por_leer != 0){
    if (file_desc -> frame == 0){ //es el primer frame que lee
      queda_por_terminar_frame = 8*1048576 - file_desc->offset - file_desc -> temp_bytes;
    }
    else{ // Esta en otro frame
      pfn = buffer_page_table[file_desc->vpn + file_desc->frame] & (~(0x01 << 7));
      queda_por_terminar_frame = 8*1048576 - file_desc -> temp_bytes;
      file_address = (pfn << 23);
      
    }

    if(n_bytes >= file_desc->size - file_desc->bytes_avanzados){ //SI es mayor o igual al archivo restante
      if(file_desc->size - file_desc->bytes_avanzados >= queda_por_terminar_frame){ //Hay que leer mas de un frame o el frame completo
        bytes_a_leer = queda_por_terminar_frame;
        falto_por_leer = (file_desc->size - file_desc->bytes_avanzados) - queda_por_terminar_frame;
        file_desc->frame++;
        fseek(fp, 4*1024 + 16 + file_address + file_desc ->temp_bytes, SEEK_SET);
        file_desc->temp_bytes = 0;
      }
      else{ // Solo se lee un frame
        bytes_a_leer = file_desc->size - file_desc->bytes_avanzados;
        falto_por_leer = 0;
        fseek(fp, 4*1024 + 16 + file_address + file_desc ->temp_bytes, SEEK_SET);
        file_desc->temp_bytes += bytes_a_leer;
      }
    }
    else{ // Si se pueden leer los n_bytes
      if (n_bytes >= queda_por_terminar_frame){ // Hay que leer mas frames o  justo todo el frame
        bytes_a_leer = queda_por_terminar_frame;
        falto_por_leer = n_bytes - queda_por_terminar_frame;
        file_desc->frame++;
        fseek(fp, 4*1024 + 16 + file_address + file_desc ->temp_bytes, SEEK_SET);
        file_desc->temp_bytes = 0;
      }
      else { // Se lee un solo frame
        bytes_a_leer = n_bytes;
        falto_por_leer = 0;
        fseek(fp, 4*1024 + 16 + file_address + file_desc ->temp_bytes, SEEK_SET);
        file_desc->temp_bytes += bytes_a_leer;
      }
    }
    fread(temp_buffer, 1, bytes_a_leer, fp);

    snprintf(buffer, n_bytes + 1, "%s", temp_buffer);

    file_desc->bytes_avanzados += bytes_a_leer;
    count_bytes += bytes_a_leer;
  }
  free(temp_buffer);
  fclose(fp);
  return count_bytes;

}

void cr_delete_file(CrmsFile* file_desc){
  fp = fopen(path, "rb+");
  unsigned char sub_buffer[21];
  unsigned char buffer_page_table[32];
  int actual_process = file_desc -> actual_process;
  int entrada = file_desc -> file_entrada;
  fseek(fp, actual_process * 256 + 14 + 21*entrada, SEEK_SET);
  u_int8_t zero=0;
  unsigned char pfn;
  fwrite(&zero, 1, 1, fp); // Invalidar archivo en PCB
  int bytes_restantes = file_desc -> size;
  unsigned char vpn = file_desc -> vpn;
  fseek(fp, file_desc->actual_process*256 + 224, SEEK_SET);
  fread(buffer_page_table, 1, 32, fp);
  int bits;
  unsigned char byte_buffer[1];

  while (bytes_restantes >= 0)
  {
    if(bytes_restantes >= (8*1024*1024 - file_desc -> offset)){ //si el tamaño del archivo pasa al siguiente frame

        fseek(fp, file_desc->actual_process*256 + 224 + vpn, SEEK_SET); // Tabla de paginas
        pfn = buffer_page_table[vpn] & (~(0x01 << 7));
        fwrite(&pfn, 1, 1, fp); // Invalida en tabla de paginas
        fseek(fp, 4*1024 + (int) pfn/8, SEEK_SET); // Bitmap
        fread(byte_buffer, 1, 1, fp); // Leemos byte que hay que cambiar
        bits = pfn%8;
        byte_buffer[0] = byte_buffer[0] & (~(0x01 << (7 - bits))); //Le cambiamos el bit que corresponde al pfn
        fseek(fp, 4*1024 + (int) pfn/8, SEEK_SET); // Bitmap
        fwrite(&byte_buffer, 1, 1, fp); // Cambia bit de validez en bitmap
    }

    vpn++;
    bytes_restantes -= (8*1024*1024 - file_desc -> offset);
    file_desc -> offset = 0;
  }

  fclose(fp);
}

void cr_close(CrmsFile* file_desc){
  printf("Se cerró el archivo %s\n", file_desc->name);
  free(file_desc);
}

int cr_write_file(CrmsFile* file_desc, void* buffer, int n_bytes)
{
  u_int32_t file_address = file_desc->address;
  u_int32_t bytes_a_leer;
  unsigned char pfn;
  unsigned char buffer_page_table[32];
  int falto_por_leer = -1;
  u_int32_t queda_por_terminar_frame;
  int escritos = 0;

  fp = fopen(path, "wb");

  if (file_desc->mode != 'w'){
    printf("Modo no está en w\n");
    //free(temp_buffer);
    return -1;
  }
  if (file_desc->size == 0)
  {
    queda_por_terminar_frame = 8*1048576 - file_desc->offset - file_desc -> temp_bytes;
    if (n_bytes <= queda_por_terminar_frame)
    {
      fseek(fp, 4*1024 + 16 + file_address ,SEEK_SET);
      fwrite(buffer, n_bytes, 1, fp);
      escritos = n_bytes;
    }
    else{
      fseek(fp, 4*1024 + 16 + file_address ,SEEK_SET);
      unsigned char buffer_cabe[queda_por_terminar_frame];
      for (int d=0; d<queda_por_terminar_frame; d++)
      {
        buffer_cabe[d] = buffer[d];
      }
      escritos += queda_por_terminar_frame;
      fwrite(buffer_cabe, queda_por_terminar_frame, 1, fp);
      pfn = buffer_page_table[file_desc->vpn + 1] & (~(0x01 << 7));
    }
  }
  
  return escritos;


}