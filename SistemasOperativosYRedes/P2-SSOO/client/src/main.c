#include <unistd.h>
#include <stdio.h>
#include "conection.h"
#include "comunication.h"

char * get_input(){
  char * response = malloc(20);
  int pos=0;
  while (1){
    char c = getchar();
    if (c == '\n') break;
    response[pos] = c;
    pos++;
  }
  response[pos] = '\0';
  return response;
  
}


int main (int argc, char *argv[]){
  //Se obtiene la ip y el puerto donde está escuchando el servidor (la ip y puerto de este cliente da igual)
  char * IP;
  int PORT;
  if (argc != 5){
    printf("Cantidad insuficiente de argumentos\n");
    printf("%s   %s\n", argv[1], argv[2]);
    return 0;
  }
  if (!strcmp(argv[1], "-i") && !strcmp(argv[3], "-p")){
    IP = argv[2];
    PORT = atoi(argv[4]);
  }
  else if (!strcmp(argv[1], "-p") && !strcmp(argv[3], "-i")){
    PORT = atoi(argv[2]);
    IP = argv[4];
  }
  else{
    printf("Formato incorrecto de argumentos\n");
    return 0;
  }

  // Se prepara el socket
  int server_socket = prepare_socket(IP, PORT);

  // Se inicializa un loop para recibir todo tipo de paquetes y tomar una acción al respecto
  while (1){
    int msg_code = client_receive_id(server_socket);

    if (msg_code == 2) { // No espera input, solo printea
      char * message = client_receive_payload(server_socket);
      printf("%s\n", message);
      free(message);
    }
    else if (msg_code == 1) { //Recibimos un mensaje del servidor
      //msg_code == 1 es cuando estamos en el lobby y todavía no empieza el juego
      char * message = client_receive_payload(server_socket);
      printf("%s\n", message);
      free(message);
      char * response = get_input();

      client_send_message(server_socket, 1, response);
      free(response);
    }
    else if (msg_code == 3) { //El jugador ya no forma parte del juego
      // Se cierra el socket
      char * message = client_receive_payload(server_socket);
      printf("%s\n", message);
      free(message);
      close(server_socket);
      //free(IP);
      return 0;
    }
  }


  return 0;
}
