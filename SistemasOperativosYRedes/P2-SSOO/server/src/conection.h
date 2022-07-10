#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include "comunication.h"
#include <pthread.h>


typedef struct players_info{
  int socket_c1;
  int socket_c2;
  int socket_c3;
  int socket_c4;
} PlayersInfo;

PlayersInfo * prepare_sockets_and_get_clients(char * IP, int port);

typedef struct jugador{
  int id;
  char * nombre;
  int socket;
  int vivo;
  int oro;
  int comida;
  int ciencia;
  int agricultores;
  int mineros;
  int ingenieros;
  int guerreros;
  int nivel_agricultores;
  int nivel_mineros;
  int nivel_ingenieros;
  int nivel_ataque;
  int nivel_defensa;
} Jugador;



PlayersInfo * sockets_clients;
PlayersInfo * players_info;
int server_socket;
struct sockaddr_in client1_addr;
struct sockaddr_in client2_addr;
struct sockaddr_in client3_addr;
struct sockaddr_in client4_addr;
socklen_t addr_size;
int players_ready;
int players_connected;
Jugador* jugadores[4];
pthread_t p2, p3, p4;
int hay_jugadores;