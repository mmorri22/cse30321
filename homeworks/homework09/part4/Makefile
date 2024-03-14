# Author: Prof. Matthew Morrison
# E-mail: matt.morrison@nd.edu
#
# This is the Makefile for the Homework 09.

CC := gcc
CFLAGS := -std=c11 -Wall

part4_OBJECTS := test_part4.o part4.o

part4: $(part4_OBJECTS)
	$(CC) $(CFLAGS) -o part4 $(part4_OBJECTS)

test_part4.o: part4.c part4.h
	$(CC) $(CFLAGS) -c test_part4.c

part4.o: part4.c part4.h
	$(CC) $(CFLAGS) -c part4.c

executables := part4

all: $(executables)

clean:
	rm -rf *.o *.swp $(executables)
