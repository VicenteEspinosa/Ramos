crms: main.o crms_API.o
	gcc main.o crms_API.o -g -o crms

main.o: main.c crms_API.h
	gcc main.c -c -o main.o

crms_API.o: crms_API.h crms_API.c
	gcc crms_API.c -c -o crms_API.o