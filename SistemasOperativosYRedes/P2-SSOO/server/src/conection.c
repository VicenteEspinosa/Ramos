#include "conection.h"

//LINKS REFERENCIAS:
//https://www.man7.org/linux/man-pages/man2/socket.2.html
//https://man7.org/linux/man-pages/man7/socket.7.html
//https://www.man7.org/linux/man-pages/man3/setsockopt.3p.html
//https://man7.org/linux/man-pages/man2/setsockopt.2.html
//https://linux.die.net/man/3/htons
//https://linux.die.net/man/3/inet_aton
//https://www.howtogeek.com/225487/what-is-the-difference-between-127.0.0.1-and-0.0.0.0/
//https://www.man7.org/linux/man-pages/man2/bind.2.html
//https://www.man7.org/linux/man-pages/man2/accept.2.html


void preguntas_iniciales(int socket, int id){
  char* payload1;
  char* payload2;
  char* payload3;
  char* payload4;
  char * mensaje = "Ingresa tu nombre"; 
  server_send_message(socket, 1, mensaje); // Pedir nombre
  int msg_code = server_receive_id(socket);
  char * name = server_receive_payload(socket); 
  char message[200] = "Se conecto: ";
  strcat(message, name);
  printf("%s\n", message);
  if (id != 1){
    server_send_message(sockets_clients->socket_c1, 2, message); // Avisar a usuario lider de nuevo jugador
  }

  int restantes = 9;
  int cantidad = -1;
  int agricultores, mineros, ingenieros, guerreros;

  while (restantes < cantidad || cantidad < 0)
  {
    char * mensaje = "Con cuantos agricultores quieres comenzar?";
    server_send_message(socket, 1, mensaje); // Pedir n° agricultores
    int msg_code = server_receive_id(socket);
    payload1 = server_receive_payload(socket);
    cantidad = atoi(payload1); // n° agricultores
    free(payload1);
    agricultores = cantidad;
  }
  restantes -= agricultores;

  cantidad = -1;
  while (restantes < cantidad || cantidad < 0){
    char * mensaje = "Con cuantos mineros quieres comenzar?";
    server_send_message(socket, 1, mensaje); // Pedir n° mineros
    int msg_code = server_receive_id(socket);
    payload2 = server_receive_payload(socket);
    cantidad = atoi(payload2); // n° mineros
    free(payload2);
    mineros = cantidad;
  }
  restantes -= mineros;

  cantidad = -1;
  while (restantes < cantidad || cantidad < 0){
    char * mensaje = "Con cuantos ingenieros quieres comenzar?";
    server_send_message(socket, 1, mensaje); // Pedir n° ingenieros
    int msg_code = server_receive_id(socket);
    payload3 = server_receive_payload(socket);
    cantidad = atoi(payload3); // n° ingenieros
    free(payload3);
    ingenieros = cantidad;
  }
  restantes -= ingenieros;

  cantidad = -1;
  while (restantes < cantidad || cantidad < 0){
    char * mensaje = "Con cuantos guerreros quieres comenzar?";
    server_send_message(socket, 1, mensaje); // Pedir n° guerreros
    int msg_code = server_receive_id(socket);
    payload4 = server_receive_payload(socket);
    cantidad = atoi(payload4); // n° guerreros
    free(payload4);
    guerreros = cantidad;
  }
  restantes -= guerreros;

  Jugador* jugador = malloc(sizeof(Jugador));
  *jugador = (Jugador) {
    .id = id,
    .nombre = name,
    .socket = socket,
    .agricultores = agricultores,
    .mineros = mineros,
    .ingenieros = ingenieros,
    .guerreros = guerreros,
    .vivo = 1,
    .oro = 0,
    .comida = 0,
    .ciencia = 0,
    .nivel_agricultores = 1,
    .nivel_ataque = 1,
    .nivel_defensa = 1,
    .nivel_ingenieros = 1,
    .nivel_mineros = 1,
  };
  jugadores[id-1] = jugador;
  printf("El jugador %i esta listo\n", id);
}

void* newPlayer(void *arg){
  if (players_connected == 1) // Llego el player 2
  {
    sockets_clients->socket_c2 = accept(server_socket, (struct sockaddr *)&client2_addr, &addr_size);
    players_connected++;
    pthread_create(&p3, NULL, newPlayer, "B");
    pthread_detach(p3);
    printf("Se conecto el jugador %i\n", players_connected);
    preguntas_iniciales(sockets_clients->socket_c2, 2);
    players_ready++;
  }
  else if (players_connected == 2) // Llego el player 3
  {
    sockets_clients->socket_c3 = accept(server_socket, (struct sockaddr *)&client3_addr, &addr_size);
    players_connected++;
    pthread_create(&p4, NULL, newPlayer, "C");
    pthread_detach(p4);
    printf("Se conecto el jugador %i\n", players_connected);
    preguntas_iniciales(sockets_clients->socket_c3, 3);
    players_ready++;


  }
  else if (players_connected == 3) // Llego el player 4
  {
    sockets_clients->socket_c4 = accept(server_socket, (struct sockaddr *)&client4_addr, &addr_size);
    players_connected++;
    printf("Se conecto el jugador %i\n", players_connected);
    preguntas_iniciales(sockets_clients->socket_c4, 4);
    players_ready++;

    
  }
  pthread_exit(NULL);
}

PlayersInfo * prepare_sockets_and_get_clients(char * IP, int port){
  // Se define la estructura para almacenar info del socket del servidor al momento de su creación
  struct sockaddr_in server_addr;

  // Se solicita un socket al SO, que se usará para escuchar conexiones entrantes
  server_socket = socket(AF_INET, SOCK_STREAM, 0);

  // Se configura el socket a gusto (recomiendo fuertemente el REUSEPORT!)
  int opt = 1;
  int ret = setsockopt(server_socket, SOL_SOCKET, SO_REUSEPORT, &opt, sizeof(opt));

  // Se guardan el puerto e IP en la estructura antes definida
  memset(&server_addr, 0, sizeof(server_addr));
  server_addr.sin_family = AF_INET;
  inet_aton(IP, &server_addr.sin_addr);
  server_addr.sin_port = htons(port);

  // Se le asigna al socket del servidor un puerto y una IP donde escuchar
  int ret2 = bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr));

  // Se coloca el socket en modo listening
  int ret3 = listen(server_socket, 1);

  // Se definen las estructuras para almacenar info sobre los sockets de los clientes
  addr_size = sizeof(client1_addr);
  players_ready = 0;
  players_connected = 0;

  // Se inicializa una estructura propia para guardar los n°s de sockets de los clientes.
  sockets_clients = malloc(sizeof(PlayersInfo));


  // Se aceptan a los primeros 2 clientes que lleguen. "accept" retorna el n° de otro socket asignado para la comunicación
  sockets_clients->socket_c1 = accept(server_socket, (struct sockaddr *)&client1_addr, &addr_size);
  server_send_message(sockets_clients->socket_c1, 2, "Fuiste el primero, eres el lider del grupo\n");
  printf("Se conecto el primer jugador\n");
  players_ready ++; players_connected++;
  pthread_create(&p2, NULL, newPlayer, "A");
  pthread_detach(p2);
  preguntas_iniciales(sockets_clients->socket_c1, 1);

  //sockets_clients->socket_c2 = accept(server_socket, (struct sockaddr *)&client2_addr, &addr_size);
  //printf("conectados: %d", players_connected);

  return sockets_clients;
}
