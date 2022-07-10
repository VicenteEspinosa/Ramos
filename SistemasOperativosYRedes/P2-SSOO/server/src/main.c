#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "comunication.h"
#include "conection.h"
#include <pthread.h>

void liberar_jugadores(){
  for (int i=0; i<players_connected; i++){
    free(jugadores[i]->nombre);
    free(jugadores[i]);
  }
  free(players_info);
  hay_jugadores = 0;
  printf("Cerrando el servidor\n");
};
                                                                                                          
void avisar_todos(char* mensaje, int code){
  for (int i =0; i<4; i++){
    if (jugadores[i] && jugadores[i]->vivo){
      server_send_message(jugadores[i]->socket, code, mensaje);
    }
  }
};

int check_final(){
  int vivos = 0;
  int ganador;
  for (int i = 0; i<players_ready; i++){
    if (jugadores[i]->vivo){
      vivos++;
      ganador = i;
    }
  }
  if (vivos <= 1){
    return ganador; // Termino
  }
  return -1;
};

void subir_nivel(int jugador){
  int msg_code;
  int opcion;
  int required;
  server_send_message(jugadores[jugador]->socket, 2, "********************** Subir de nivel ***************************");
  char* menu = "Elige el aspecto a mejorar de tu Aldea:\n"
      " 1) Nivel agricultores\n 2) Nivel mineros\n"
      " 3) Nivel ingenieros\n 4) Nivel ataque\n"
      " 5) Nivel defensa\n 6) Volver al menu";

  server_send_message(jugadores[jugador]->socket, 1, menu);
  msg_code = 0;
  while (msg_code != 1){
    msg_code = server_receive_id(jugadores[jugador]->socket); // Esperar hasta que el jugador mande msg_code == 1
  }
  char * payload = server_receive_payload(jugadores[jugador]->socket);
  opcion = atoi(payload);
  free(payload);
  if (opcion == 1){
    required = 10 * (jugadores[jugador]->nivel_agricultores);
    if (
      jugadores[jugador]->oro >= required
      && jugadores[jugador]->ciencia >= required 
      && jugadores[jugador]->comida >= required 
      && jugadores[jugador] -> nivel_agricultores < 5
      ){
      jugadores[jugador] -> nivel_agricultores +=1;
      jugadores[jugador] -> oro -= required;
      jugadores[jugador] -> ciencia -= required;
      jugadores[jugador] -> comida-= required;
      int length1 = snprintf( NULL, 0, "%d", jugadores[jugador]->nivel_agricultores );
      char* str1 = malloc( length1 + 1 );
      snprintf( str1, length1 + 1, "%d", jugadores[jugador]->nivel_agricultores );
      char message_1[] = "Felicitaciones! tu nivel de agricultura ha subido a: ";
      strcat(message_1, str1);
      server_send_message(jugadores[jugador]->socket, 2, message_1);
      free(str1);
    } else {
      server_send_message(jugadores[jugador]->socket, 2, "No tienes los recursos necesarios para realizar esa acción\n\n");
      subir_nivel(jugador);
    }
  }
  else if (opcion == 2){
    required = 10 * (jugadores[jugador]->nivel_mineros);
    if (
      jugadores[jugador]->oro >= required
      && jugadores[jugador]->ciencia >= required 
      && jugadores[jugador]->comida >= required 
      && jugadores[jugador] -> nivel_mineros < 5
      ){
      jugadores[jugador] -> nivel_mineros +=1;
      jugadores[jugador] -> oro -= required;
      jugadores[jugador] -> ciencia -= required;
      jugadores[jugador] -> comida-= required;
      int length1 = snprintf( NULL, 0, "%d", jugadores[jugador]->nivel_mineros );
      char* str1 = malloc( length1 + 1 );
      snprintf( str1, length1 + 1, "%d", jugadores[jugador]->nivel_mineros );
      char message_1[] = "Felicitaciones! tu nivel de mineria ha subido a: ";
      strcat(message_1, str1);
      server_send_message(jugadores[jugador]->socket, 2, message_1);
      free(str1);
    } else {
      server_send_message(jugadores[jugador]->socket, 2, "No puedes realizar esta acción\n\n");
      subir_nivel(jugador);
    }

  }
  else if (opcion == 3){
    required = 10 * (jugadores[jugador]->nivel_ingenieros);
    if (
      jugadores[jugador]->oro >= required
      && jugadores[jugador]->ciencia >= required 
      && jugadores[jugador]->comida >= required 
      && jugadores[jugador] -> nivel_ingenieros < 5
      ){
      jugadores[jugador] -> nivel_ingenieros +=1;
      jugadores[jugador] -> oro -= required;
      jugadores[jugador] -> ciencia -= required;
      jugadores[jugador] -> comida-= required;
      int length1 = snprintf( NULL, 0, "%d", jugadores[jugador]->nivel_ingenieros );
      char* str1 = malloc( length1 + 1 );
      snprintf( str1, length1 + 1, "%d", jugadores[jugador]->nivel_ingenieros );
      char message_1[] = "Felicitaciones! tu nivel de ingenieria ha subido a: ";
      strcat(message_1, str1);
      server_send_message(jugadores[jugador]->socket, 2, message_1);
      free(str1);
    } else {
      server_send_message(jugadores[jugador]->socket, 2, "No tienes los recursos necesarios para realizar esa acción\n\n");
      subir_nivel(jugador);
    }  
  }
  else if (opcion == 4){
    required = 10 * (jugadores[jugador]->nivel_ataque);
    if (
      jugadores[jugador]->oro >= required
      && jugadores[jugador]->ciencia >= required 
      && jugadores[jugador]->comida >= required 
      && jugadores[jugador] -> nivel_ataque < 5
      ){
      jugadores[jugador] -> nivel_ataque +=1;
      jugadores[jugador] -> oro -= required;
      jugadores[jugador] -> ciencia -= required;
      jugadores[jugador] -> comida-= required;
      int length1 = snprintf( NULL, 0, "%d", jugadores[jugador]->nivel_ataque);
      char* str1 = malloc( length1 + 1 );
      snprintf( str1, length1 + 1, "%d", jugadores[jugador]->nivel_ataque );
      char message_1[] = "Felicitaciones! tu nivel de ataque ha subido a: ";
      strcat(message_1, str1);
      server_send_message(jugadores[jugador]->socket, 2, message_1);
      free(str1);
    } else {
      server_send_message(jugadores[jugador]->socket, 2, "No tienes los recursos necesarios para realizar esa acción\n\n");
      subir_nivel(jugador);
    }  
  }
  else if (opcion == 5){
    required = 10 * (jugadores[jugador]->nivel_defensa);
    if (
      jugadores[jugador]->oro >= required
      && jugadores[jugador]->ciencia >= required 
      && jugadores[jugador]->comida >= required 
      && jugadores[jugador] -> nivel_defensa < 5
      ){
      jugadores[jugador] -> nivel_defensa +=1;
      jugadores[jugador] -> oro -= required;
      jugadores[jugador] -> ciencia -= required;
      jugadores[jugador] -> comida-= required;
      int length1 = snprintf( NULL, 0, "%d", jugadores[jugador]->nivel_defensa );
      char* str1 = malloc( length1 + 1 );
      snprintf( str1, length1 + 1, "%d", jugadores[jugador]->nivel_defensa );
      char message_1[] = "Felicitaciones! tu nivel de defensa ha subido a: ";
      strcat(message_1, str1);
      server_send_message(jugadores[jugador]->socket, 2, message_1);
      free(str1);
    } else {
      server_send_message(jugadores[jugador]->socket, 2, "No tienes los recursos necesarios para realizar esa acción\n\n");
      subir_nivel(jugador);
    }
  }
  else if (opcion == 6){
    //desplegar el menu
  } else {
    server_send_message(jugadores[jugador]->socket, 2, "Elige una opción válida!\n\n");
    subir_nivel(jugador);
  }
};
void atacar(int jugador){
  int msg_code;
  int opcion;
  int index = 0;


  server_send_message(jugadores[jugador]->socket, 2, "\n**************************ATACAR**************************\n");
  server_send_message(jugadores[jugador]->socket, 2, "Elige la aldea que quieres atacar:\n");

  for (int i=0; i<players_ready; i++){
    if (jugadores[i]->vivo && i != jugador){
      index++;
      char message[200] = "";
      char index_str[50];
      sprintf(index_str, "%d", index);
      strcat(message, index_str);
      strcat(message, ") ");
      strcat(message, jugadores[i]->nombre);
      server_send_message(jugadores[jugador]->socket, 2, message);
    }
  }
  index++;
  char message[200] = "";
  char index_str[50];
  sprintf(index_str, "%d", index);
  strcat(message, index_str);
  strcat(message, ") ");
  strcat(message, "Volver\n");
  server_send_message(jugadores[jugador]->socket, 1, message);

  msg_code = 0;
  while (msg_code != 1){
    msg_code = server_receive_id(jugadores[jugador]->socket); // Esperar hasta que el jugador mande msg_code == 1
  }
  char* payload = server_receive_payload(jugadores[jugador]->socket);
  opcion = atoi(payload);
  free(payload);

  int index_atacado = -1;
  int index2 = -1;
  for (int i=1; i<index; i++){
    index2 ++; // Index de jugador que marca la opcion i
    while (!jugadores[index2]->vivo){
      index2++;
    }
    if (index2 == jugador){ // Saltar a si mismo
      index2++;
      while(!jugadores[index2]->vivo){
        index2++;
      }
    }
    if (opcion == i){
      index_atacado = index2;
    }
  }

  if (index_atacado != -1){

    int ataque = jugadores[jugador]->guerreros * jugadores[jugador]->nivel_ataque;
    int defensa = jugadores[index_atacado]->guerreros * jugadores[index_atacado]->nivel_defensa * 2;

    char message[200] = "";
    strcat(message, jugadores[jugador]->nombre);
    strcat(message, " ataco a ");
    strcat(message, jugadores[index_atacado]->nombre);



    if (ataque > defensa){
      jugadores[jugador]->oro += jugadores[index_atacado]->oro;
      jugadores[jugador]->comida += jugadores[index_atacado]->comida;
      jugadores[jugador]->ciencia += jugadores[index_atacado]->ciencia;
      jugadores[index_atacado]->vivo = 0;

      strcat(message, " y gano!\n");
      strcat(message, jugadores[index_atacado]->nombre);
      strcat(message, " fue eliminado\n");


      avisar_todos(message, 2);

      jugadores[index_atacado]->vivo = 0;
      char message2[200] = "Fuiste atacado por  ";
      strcat(message2, jugadores[jugador]->nombre);
      strcat(message2, " y te elimino :(\n");
      server_send_message(jugadores[index_atacado]->socket, 3, message2); // Eliminar al jugador del juego
      close(jugadores[index_atacado]->socket);
      char message[200] = "El jugador ";
      strcat(message, jugadores[index_atacado]->nombre);
      strcat(message, " fue derrotado");
      avisar_todos(message, 2);
      int ganador = check_final();
      if (ganador != -1){
        server_send_message(jugadores[ganador]->socket, 3, "Felicidades! Ganaste!\n\n");
        close(jugadores[ganador]->socket);
        liberar_jugadores();
      }
    }
    else{
      printf("Pierde %i tropas\n", jugadores[jugador]->guerreros/2);
      jugadores[jugador]->guerreros -= jugadores[jugador]->guerreros/2;
      printf("Ahora tiene %i tropas\n", jugadores[jugador]->guerreros);

      strcat(message, " y perdio!\n");
      strcat(message, jugadores[jugador]->nombre);
      strcat(message, " perdio tropas al intentar\n");
      avisar_todos(message, 2);

    }
  }
};
void crear_aldeano(int jugador){
  int client_code = 0;
  char* creation_options = "Elige qué tipo de aldeano quierer crear:\n"
      " 1) Agricultor\n 2) Minero\n"
      " 3) Ingeniero\n 4) Guerrero\n";

  
  server_send_message(jugadores[jugador]->socket, 2, "\n**************************CREAR ALDEANO**************************\n");

  server_send_message(jugadores[jugador]->socket, 1, creation_options);

  while (client_code != 1){
    client_code = server_receive_id(jugadores[jugador]->socket); // Esperar hasta que el jugador mande msg_code == 1
  }
  char* payload = server_receive_payload(jugadores[jugador]->socket);
  int chosen_type = atoi(payload);
  free(payload);

  if (chosen_type == 1){ // Crear agricultor
    if(jugadores[jugador]->comida >= 10){ //se puede crear el agricultor
      char message[200] = "";
      char player_number[50];
      jugadores[jugador]-> comida -= 10;
      jugadores[jugador] -> agricultores ++;
      char* success_message = "Has creado un aldeano agricultor.\n";
      server_send_message(jugadores[jugador]->socket, 2, success_message);
    }
    else{
      char* fail_message = "No tienes los recursos necesarios para crear un aldeano agricultor.\n";
      server_send_message(jugadores[jugador]->socket, 2, fail_message);
    }
  }
  else if (chosen_type== 2){ // Crear minero
    if(jugadores[jugador]->comida >= 10 && jugadores[jugador]->oro >= 5){ //se puede crear el minero
        char message[200] = "";
        char player_number[50];
        jugadores[jugador]-> comida -= 10;
        jugadores[jugador]-> oro -= 5;
        jugadores[jugador] -> mineros ++;
        char* success_message = "Has creado un aldeano minero.\n";
        server_send_message(jugadores[jugador]->socket, 2, success_message);
      }
      else{
        char* fail_message = "No tienes los recursos necesarios para crear un aldeano minero.\n";
        server_send_message(jugadores[jugador]->socket, 2, fail_message);
      }
  }
  else if (chosen_type == 3){ // Crear ingeniero
    if(jugadores[jugador]->comida >= 20 && jugadores[jugador]->oro >= 10){ //se puede crear el ingeniero
          char message[200] = "";
          char player_number[50];
          jugadores[jugador]-> comida -= 20;
          jugadores[jugador]-> oro -= 10;
          jugadores[jugador] -> ingenieros ++;
          char* success_message = "Has creado un aldeano ingeniero.\n";
          server_send_message(jugadores[jugador]->socket, 2, success_message);
        }
        else{
          char* fail_message = "No tienes los recursos necesarios para crear un aldeano ingeniero.\n";
          server_send_message(jugadores[jugador]->socket, 2, fail_message);
        }
  }
  else if (chosen_type == 4){ // Crear guerrero
     if(jugadores[jugador]->comida >= 10 && jugadores[jugador]->oro >= 10){ //se puede crear el guerrero
          char message[200] = "";
          char player_number[50];
          jugadores[jugador]-> comida -= 10;
          jugadores[jugador]-> oro -= 10;
          jugadores[jugador] -> guerreros ++;
          char* success_message = "Has creado un aldeano guerrero.\n";
          server_send_message(jugadores[jugador]->socket, 2, success_message);
        }
        else{
          char* fail_message = "No tienes los recursos necesarios para crear un aldeano guerrero.\n";
          server_send_message(jugadores[jugador]->socket, 2, fail_message);
        }
  }
};
void mostrar_info(int jugador){
  //Se debe mostrar; 
  //Cantidad de cada recurso (oro, comida y ciencia)
  //Cantidad de aldeanos en cada rol (Agricultores, mineros, ingenieros, guerreros)
  //Nivel de agricultores, mineros, ingenieros, ataque y defensa.
  int oro = jugadores[jugador]->oro;
  int com = jugadores[jugador]->comida;
  int cie = jugadores[jugador]->ciencia;
  int agricultores = jugadores[jugador]->agricultores;
  int mineros = jugadores[jugador]->mineros;
  int ingenieros = jugadores[jugador]->ingenieros;
  int guerreros = jugadores[jugador]->guerreros;
  int nivel_agricultores = jugadores[jugador]->nivel_agricultores; 
  int nivel_mineros = jugadores[jugador]->nivel_mineros;
  int nivel_ingenieros = jugadores[jugador]->nivel_ingenieros;
  int nivel_ataque = jugadores[jugador]->nivel_ataque ;
  int nivel_defensa = jugadores[jugador]->nivel_defensa;


  int length1 = snprintf( NULL, 0, "%d", oro );
  char* soro = malloc( length1 + 1 );
  snprintf( soro, length1 + 1, "%d", oro ); 

  int length2 = snprintf( NULL, 0, "%d", com );
  char* scom = malloc( length2 + 1 );
  snprintf( scom, length2 + 1, "%d", com ); 

  int length3 = snprintf( NULL, 0, "%d", cie );
  char* scie = malloc( length3 + 1 );
  snprintf( scie, length3 + 1, "%d", cie ); 

  int length4 = snprintf( NULL, 0, "%d", agricultores );
  char* sagricultores = malloc( agricultores + 1 );
  snprintf( sagricultores, length4 + 1, "%d", agricultores ); 

  int length5 = snprintf( NULL, 0, "%d", mineros );
  char* smineros = malloc( mineros + 1 );
  snprintf( smineros, length5 + 1, "%d", mineros ); 

  int length6 = snprintf( NULL, 0, "%d", ingenieros );
  char* singenieros = malloc( ingenieros + 1 );
  snprintf( singenieros, length6 + 1, "%d", ingenieros ); 

  int length7 = snprintf( NULL, 0, "%d", guerreros );
  char* sguerreros = malloc( guerreros + 1 );
  snprintf( sguerreros, length7 + 1, "%d", guerreros ); 

  int length8 = snprintf( NULL, 0, "%d", nivel_agricultores );
  char* snivel_agricultores = malloc( nivel_agricultores+ 1 );
  snprintf( snivel_agricultores, length8 + 1, "%d", nivel_agricultores ); 

  int length9 = snprintf( NULL, 0, "%d", nivel_ingenieros );
  char* snivel_ingenieros = malloc( nivel_ingenieros + 1 );
  snprintf( snivel_ingenieros, length9 + 1, "%d", nivel_ingenieros ); 

  int length10 = snprintf( NULL, 0, "%d", nivel_mineros );
  char* snivel_mineros = malloc( nivel_mineros + 1 );
  snprintf( snivel_mineros, length10 + 1, "%d", nivel_mineros ); 

  int length11 = snprintf( NULL, 0, "%d", nivel_ataque );
  char* snivel_ataque = malloc( nivel_ataque + 1 );
  snprintf( snivel_ataque, length11 + 1, "%d", nivel_ataque ); 

  int length12 = snprintf( NULL, 0, "%d", nivel_defensa );
  char* snivel_defensa = malloc( nivel_defensa + 1 );
  snprintf( snivel_defensa, length12 + 1, "%d", nivel_defensa ); 


  char recursos1[200] = "*********************** Tus recursos: ************************* ";
  char mensaje_oro[20] = "Oro : ";
  char mensaje_comida[20] = "Comida : ";
  char mensaje_ciencia[20] = "Ciencia : ";
  char recursos2[200] = "********************** Tus aldeanos *************************** ";
  char mensaje_agricultores[200] = "Cantidad de agricultores : "; 
  char mensaje_mineros[200] = "Cantidad de mineros : "; 
  char mensaje_ingenieros[200] = "Cantidad de ingenieros : "; 
  char mensaje_guerreros[200] = "Cantidad de guerreros : "; 
  char recursos3[200] = "************************************************************** ";
  strcat(mensaje_oro, soro);
  strcat(mensaje_comida, scom);
  strcat(mensaje_ciencia, scie);
  strcat(mensaje_agricultores, sagricultores);
  strcat(mensaje_agricultores, " | Nivel: ");
  strcat(mensaje_agricultores, snivel_agricultores);
  strcat(mensaje_mineros, smineros);
  strcat(mensaje_mineros, " | Nivel: ");
  strcat(mensaje_mineros, snivel_mineros);
  strcat(mensaje_ingenieros, singenieros);
  strcat(mensaje_ingenieros, " | Nivel: ");
  strcat(mensaje_ingenieros, snivel_ingenieros);
  strcat(mensaje_guerreros, sguerreros);
  strcat(mensaje_guerreros, " | Nivel Ataque: ");
  strcat(mensaje_guerreros, snivel_ataque);
  strcat(mensaje_guerreros, " |  Nivel Defensa: ");
  strcat(mensaje_guerreros, snivel_defensa);

  //strcat(message_1, message_2);
  //strcat(message_1, message_3);
  free(soro);
  free(scom);
  free(scie);
  free(sagricultores);
  free(smineros);
  free(singenieros);
  free(sguerreros);
  free(snivel_agricultores);
  free(snivel_mineros);
  free(snivel_ingenieros);
  free(snivel_ataque);
  free(snivel_defensa);

  server_send_message(jugadores[jugador]->socket, 2, recursos1);
  server_send_message(jugadores[jugador]->socket, 2, mensaje_oro);
  server_send_message(jugadores[jugador]->socket, 2, mensaje_comida);
  server_send_message(jugadores[jugador]->socket, 2, mensaje_ciencia);
  server_send_message(jugadores[jugador]->socket, 2, recursos2);
  server_send_message(jugadores[jugador]->socket, 2, mensaje_agricultores);
  server_send_message(jugadores[jugador]->socket, 2, mensaje_mineros);
  server_send_message(jugadores[jugador]->socket, 2, mensaje_ingenieros);
  server_send_message(jugadores[jugador]->socket, 2, mensaje_guerreros);
  server_send_message(jugadores[jugador]->socket, 2, recursos3);

}

void recolectar_recursos(int jugador){
  // Oro: cantidad de mineros × nivel mineros × 2
  //Comida: cantidad de agricultores × nivel agricultores × 2
  //Ciencia: cantidad de ingenieros × nivel ingenieros
  int oro_recibido = jugadores[jugador]->mineros * jugadores[jugador]->nivel_mineros * 2;
  int comida_recibida = jugadores[jugador]->agricultores * jugadores[jugador]->nivel_agricultores * 2;
  int ciencia_recibida = jugadores[jugador]->ingenieros * jugadores[jugador]->nivel_ingenieros;
  jugadores[jugador]->oro += oro_recibido;
  jugadores[jugador]->comida += comida_recibida;
  jugadores[jugador]->ciencia += ciencia_recibida;
  int oro_help = oro_recibido;
  int com_help = comida_recibida;
  int cie_help = ciencia_recibida;
  int length1 = snprintf( NULL, 0, "%d", oro_help );
  char* str1 = malloc( length1 + 1 );
  snprintf( str1, length1 + 1, "%d", oro_help );
  int length2 = snprintf( NULL, 0, "%d", com_help );
  char* str2 = malloc( length2 + 1 );
  snprintf( str2, length2 + 1, "%d", com_help );
  int length3 = snprintf( NULL, 0, "%d", cie_help );
  char* str3 = malloc( length3 + 1 );
  snprintf( str3, length3 + 1, "%d", cie_help );
  char message_1[] = "Cantidad de oro recibida : ";
  char message_2[] = "Cantidad de comida recibida : ";
  char message_3[] = "Cantidad de ciencia recibida : ";
  strcat(message_1, str1);
  strcat(message_2, str2);
  strcat(message_3, str3);
  free(str1);
  free(str2);
  free(str3);
  server_send_message(jugadores[jugador]->socket, 2, message_1);
  server_send_message(jugadores[jugador]->socket, 2, message_2);
  server_send_message(jugadores[jugador]->socket, 2, message_3);
};

void espiar(int jugador){
  int msg_code;
  int opcion;
  if (jugadores[jugador]->oro >= 30){
    server_send_message(jugadores[jugador]->socket, 2, "**************************ESPIAR**************************");
    server_send_message(jugadores[jugador]->socket, 2, "Elige la aldea que quieres espiar:");
    for (int j=0; j<players_ready; j++){
      if(jugadores[j]->vivo && j != jugador)
      {
        char messagef[] = " ";
        int num = jugadores[j]->id;
        int length = snprintf( NULL, 0, "%d", num );
        char* str = malloc( length + 1 );
        snprintf( str, length + 1, "%d", num );
        char* nombre_aldea = jugadores[j]->nombre;
        strcat(messagef, str);
        strcat(messagef, ". ");
        strcat(messagef, nombre_aldea);
        free(str);
        server_send_message(jugadores[jugador]->socket, 2, messagef);
      }
    }
    server_send_message(jugadores[jugador]->socket, 2, " 5. Volver");
    server_send_message(jugadores[jugador]->socket, 1, "Input: ");
    msg_code = 0;
    while (msg_code != 1){
      msg_code = server_receive_id(jugadores[jugador]->socket); // Esperar hasta que el jugador mande msg_code == 1
    }
    char* payload = server_receive_payload(jugadores[jugador]->socket);
    opcion = atoi(payload);
    free(payload);
    if (opcion != 5){
      jugadores[jugador]->oro -= 30;
      int n_guerreros = jugadores[opcion-1]->guerreros;
      int lvl_ataque = jugadores[opcion-1]->nivel_ataque;
      int lvl_defensa = jugadores[opcion-1]->nivel_defensa;
      int length1 = snprintf( NULL, 0, "%d", n_guerreros );
      char* str1 = malloc( length1 + 1 );
      snprintf( str1, length1 + 1, "%d", n_guerreros );
      int length2 = snprintf( NULL, 0, "%d", lvl_ataque );
      char* str2 = malloc( length2 + 1 );
      snprintf( str2, length2 + 1, "%d", lvl_ataque );
      int length3 = snprintf( NULL, 0, "%d", lvl_defensa );
      char* str3 = malloc( length3 + 1 );
      snprintf( str3, length3 + 1, "%d", lvl_defensa );
      char message_1[200] = "Número de guerreros: ";
      char message_2[200] = "Nivel de Ataque: ";
      char message_3[200] = "Nivel de Defensa: ";
      strcat(message_1, str1);
      strcat(message_2, str2);
      strcat(message_3, str3);
      free(str1);
      free(str2);
      free(str3);
      server_send_message(jugadores[jugador]->socket, 2, message_1);
      server_send_message(jugadores[jugador]->socket, 2, message_2);
      server_send_message(jugadores[jugador]->socket, 2, message_3);
      server_send_message(jugadores[jugador]->socket, 2, "************************************************************");
    }
    else{
      server_send_message(jugadores[jugador]->socket, 2, "************************************************************");
    }
  }
  else{
    server_send_message(jugadores[jugador]->socket, 2, "No tienes suficiente oro para espiar.");
    server_send_message(jugadores[jugador]->socket, 2, "************************************************************");
  }
}

void robar(int jugador){
  int msg_code;
  int opcion_jugador;
  int opcion_recurso;
  if (jugadores[jugador]->ciencia >= 10){
    server_send_message(jugadores[jugador]->socket, 2, "**************************ROBAR**************************");
    server_send_message(jugadores[jugador]->socket, 2, "Elige al jugador que le quieres robar: ");
    for (int j=0; j<players_ready; j++){
      if(jugadores[j]->vivo && j != jugador)
      {
        char messagef[200] = " ";
        int num = jugadores[j]->id;
        int length = snprintf( NULL, 0, "%d", num );
        char* str = malloc( length + 1 );
        snprintf( str, length + 1, "%d", num );
        char* nombre_aldea = jugadores[j]->nombre;
        strcat(messagef, str);
        strcat(messagef, ". ");
        strcat(messagef, nombre_aldea);
        free(str);
        server_send_message(jugadores[jugador]->socket, 2, messagef);
      }
    }
    server_send_message(jugadores[jugador]->socket, 2, " 5. Volver");
    server_send_message(jugadores[jugador]->socket, 1, "Input: ");


    msg_code = 0;
    while (msg_code != 1){
      msg_code = server_receive_id(jugadores[jugador]->socket); // Esperar hasta que el jugador mande msg_code == 1
    }
    char* payload = server_receive_payload(jugadores[jugador]->socket);
    opcion_jugador = atoi(payload);
    free(payload);
    if (opcion_jugador != 5) {
        server_send_message(jugadores[jugador]->socket, 2, "************************************************************");
        char* menu1 = "Elige qué recurso quieres robar:\n"
        " 1) Oro\n 2) Comida\n"
        " Input: ";  
      server_send_message(jugadores[jugador]->socket, 1, menu1);
      msg_code = 0;
      while (msg_code != 1){
        msg_code = server_receive_id(jugadores[jugador]->socket); // Esperar hasta que el jugador mande msg_code == 1
      }
      char * payload = server_receive_payload(jugadores[jugador]->socket);
      opcion_recurso = atoi(payload); //1 Comida , 2 Oro.
      free(payload);
      char * nombre_ladron = jugadores[jugador]->nombre;
      char * nombre_victima = jugadores[opcion_jugador-1]->nombre;
      if (opcion_recurso == 1){
        int oro_rival = jugadores[opcion_recurso-1]->oro;
        if (oro_rival > 0){
          int oro_robado;
          jugadores[jugador]->ciencia -= 10; 
          jugadores[jugador]->oro += (oro_rival/10) + 1; //Se le da el oro al que roba
          jugadores[opcion_jugador-1]->oro -= (oro_rival/10) + 1; //Se le quita oro a la víctima del robo
          oro_robado = (oro_rival/10) + 1;

          char message_oro_robado[200] = "Robo exitoso. Has robado la siguiente cantidad de oro: ";
          int length1_oro_robado = snprintf( NULL, 0, "%d", oro_robado );
          char* str1_oro_robado = malloc( length1_oro_robado + 1 );
          snprintf( str1_oro_robado, length1_oro_robado + 1, "%d", oro_robado );
          strcat(message_oro_robado, str1_oro_robado);
          strcat(message_oro_robado, "\n");

          char message_general_oro[200] = "El jugador ";
          strcat(message_general_oro, nombre_ladron );
          char message_general_oro1[200] = " le ha robado ";
          strcat(message_general_oro, message_general_oro1 );
          char message_general_oro2[200] = " al jugador ";
          strcat(message_general_oro,message_general_oro2);
          strcat(message_general_oro,nombre_victima);
          strcat(message_general_oro," ");
          strcat(message_general_oro,str1_oro_robado);
          char message_general_oro3[200] = " monedas de oro \n";
          strcat(message_general_oro,message_general_oro3);


          
          free(str1_oro_robado);

          server_send_message(jugadores[jugador]->socket, 2, message_oro_robado);
          avisar_todos(message_general_oro,2); //Cambiar mensaje
        }
        else{
          server_send_message(jugadores[jugador]->socket, 2, "No será posible robar, el jugador no tiene oro");
        }
      }
      else if (opcion_recurso == 2){
        int comida_rival = jugadores[opcion_recurso-1]->comida;
          int comida_robada;
          jugadores[jugador]->ciencia -= 10;
          jugadores[jugador]->comida += (comida_rival/10) + 1; //Se le da el oro al que roba
          jugadores[opcion_jugador-1]->comida -= (comida_rival/10) + 1;  //Se le quita oro a la víctima del robo
          comida_robada = (comida_rival/10) +1;

          if (comida_rival > 0){
          int length1_comida_robada = snprintf( NULL, 0, "%d", comida_robada );
          char* str1_comida_robada = malloc( length1_comida_robada + 1 );
          snprintf( str1_comida_robada, length1_comida_robada + 1, "%d", comida_robada );
          char message_comida_robada[200] = " Robo exitoso. Has robado la siguiente cantidad de comida: ";
          strcat(message_comida_robada, str1_comida_robada);
          strcat(message_comida_robada, "\n");
          char message_general_comida[200] = "El jugador ";
          strcat(message_general_comida, nombre_ladron );
          char message_general_comida1[200] = " le ha robado ";
          strcat(message_general_comida, message_general_comida1 );
          char message_general_comida2[200] = " al jugador ";
          strcat(message_general_comida,message_general_comida2);
          strcat(message_general_comida,nombre_victima);
          strcat(message_general_comida," ");
          strcat(message_general_comida,str1_comida_robada);
          char message_general_comida3[200] = " unidades de comida\n";
          strcat(message_general_comida,message_general_comida3);



          free(str1_comida_robada);

          server_send_message(jugadores[jugador]->socket, 2, message_comida_robada);
          avisar_todos(message_general_comida, 2); //Cambiar mensaje
          }
        else{
          server_send_message(jugadores[jugador]->socket, 2, "No será posible robar, el jugador no tiene comida");
        }
      }

    }
    else {
      server_send_message(jugadores[jugador]->socket, 2, "************************************************************");
    }

  }
  else {
    server_send_message(jugadores[jugador]->socket, 2, "No tienes suficiente ciencia para robar.");
    server_send_message(jugadores[jugador]->socket, 2, "************************************************************");
  }

}


void desplegar_menu(int i){
  if (hay_jugadores){
    int msg_code;
    int opcion;
    char* menu = "Elige una de las acciones:\n"
        " 1) Mostrar información\n 2) Crear aldeano\n"
        " 3) Subir de nivel\n 4) Atacar\n"
        " 5) Espiar\n 6) Robar\n 7) Pasar\n"
        " 8) Rendirse \n" 
        " Input: ";

    server_send_message(jugadores[i]->socket, 1, menu);
    msg_code = 0;
    while (msg_code != 1){
      msg_code = server_receive_id(jugadores[i]->socket); // Esperar hasta que el jugador mande msg_code == 1
    }
    char* payload = server_receive_payload(jugadores[i]->socket);
    opcion = atoi(payload);
    free(payload);
    if (opcion == 1){ // Mostrar información
      mostrar_info(i);
      desplegar_menu(i);
    
    }
    else if (opcion == 2){ // Crear aldeano
      crear_aldeano(i);
      desplegar_menu(i);
    }
    else if (opcion == 3){ // Subir de nivel
      subir_nivel(i);
      desplegar_menu(i);
    }
    else if (opcion == 4){ // Atacar
      atacar(i);
      desplegar_menu(i);
    }
    else if (opcion == 5){ // Espiar
      espiar(i);
      desplegar_menu(i);
    }
    else if (opcion == 6){ // Robar
      robar(i);
      desplegar_menu(i);
    }
    else if (opcion == 7){ // Pasar
      
    }
    else if (opcion == 8){ // Rendirse
      jugadores[i]->vivo = 0;
      server_send_message(jugadores[i]->socket, 3, "Te has rendido! Gracias por jugar!\n\n"); // Eliminar al jugador del juego
      close(jugadores[i]->socket);
      char message[200] = "El jugador ";
      strcat(message, jugadores[i]->nombre);
      strcat(message, " se ha rendido");
      avisar_todos(message, 2);
      int ganador = check_final();
      if (ganador != -1){
        server_send_message(jugadores[ganador]->socket, 3, "Felicidades! Ganaste!\n\n");
        close(jugadores[ganador]->socket);
        liberar_jugadores();
      }
    }
    else{ // No valido
      server_send_message(jugadores[i]->socket, 2, "Elige una opción válida!\n\n");
      desplegar_menu(i);
    }
  }
}

void empezar_juego(){
  int msg_code;
  int opcion;
  while(hay_jugadores){
    for (int i=0; i< players_ready; i++){
      if (hay_jugadores){
        if (jugadores[i]->vivo){
          recolectar_recursos(i);
          server_send_message(jugadores[i]->socket, 2, "Comenzó tu turno\n");

          desplegar_menu(i);
        


          
        }
      }
    }
  }
};

int main(int argc, char *argv[]){
  // Se define una IP y un puerto
  hay_jugadores = 1;
  char * IP;
  int PORT;
  if (argc != 5){
    printf("Cantidad insuficiente de argumentos\n");
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

  // Se crea el servidor y se obtienen los sockets de ambos clientes.
  players_info = prepare_sockets_and_get_clients(IP, PORT);

  // Le enviamos al primer cliente un mensaje de bienvenida
  //char * welcome = "Bienvenido Cliente 1!!";
  //server_send_message(players_info->socket_c1, 1, welcome);

  // Guardaremos los sockets en un arreglo e iremos alternando a quién escuchar.
  //int sockets_array[2] = {players_info->socket_c1, players_info->socket_c2};
  int sockets_array[4] = {players_info->socket_c1,0,0,0};
  int my_attention = 0;
  int jugando = 0;


  char * welcome = "1) Empezar el juego";  
  server_send_message(players_info->socket_c1, 1, welcome);
  while (hay_jugadores)
  {
    // Se obtiene el paquete del cliente 1
    int msg_code = server_receive_id(sockets_array[my_attention]);
    if (msg_code == 1){
      if (!jugando) // Lobby
      {
        jugando = players_ready > 1 && players_ready == players_connected;
        if (!jugando){
          char * response = "No hay jugadores suficientes para comenzar el juego o no todos estan listos.\n 1) Empezar el juego";
          server_send_message(players_info->socket_c1, 1, response);
        }
        else{
          printf("Se puede jugar\n");
          int non_players = 4 - players_ready; // Revisamos los jugadores que no llegaron
          if (non_players == 1){ // Llegaron 3
            jugadores[3] = NULL;
            pthread_cancel(p4); // Cancelar thread 4
          }
          else if (non_players == 2){ // Llegaron 2
            jugadores[3] = NULL;
            jugadores[2] = NULL;
            pthread_cancel(p3); // Cancelar thread 3
          }
          char* mensaje = "Va a comenzar el juego!\n";
          int code = 2;
          empezar_juego();
        }
      }
    }
    // if (jugando) // Empezo el juego
    // {
    //   printf("Llego a la 92\n");
    //   char* mensaje = "Mensaje de prueba";
    //   int code = 2;
    //   avisar_todos(mensaje, code);
    //   //empezar_juego();
    //   return 0;
    // }
  }

  return 0;
}