# Author: Prof. Matthew Morrison
# E-mail: matt.morrison@nd.edu
#
# This is the Makefile for the Lecture 23 Example.

# gcc is for the compiler for C
CC := gcc
CFLAGS := -std=c11 -Wall -Wextra -Wconversion -fopenmp -Werror
LDFLAGS := -fopenmp

executables := hello v_add dotp

# Create the Hello Library
hello.o: hello.c
	$(CC) $(CFLAGS) -c hello.c

hello: hello.o
	$(CC) $(CFLAGS) -o hello hello.o


# Dot Product
dotp_objs := dotp.o omp_apps.o

dotp.o: dotp.c
	$(CC) $(CFLAGS) -c dotp.c

omp_apps.o: omp_apps.c
	$(CC) $(CFLAGS) -c omp_apps.c

dotp: $(dotp_objs)
	$(CC) $(CFLAGS) -o dotp $(dotp_objs)


# Vector Addition
v_add_objs := v_add.o omp_apps.o

v_add.o: v_add.c
	$(CC) $(CFLAGS) -c v_add.c

v_add: $(v_add_objs)
	$(CC) $(CFLAGS) -o v_add $(v_add_objs)

# Make all
all: $(executables)

# Make clean
clean:
	rm -rf *.o *.swp $(executables)
