# Author: Prof. Matthew Morrison
# E-mail: matt.morrison@nd.edu
#
# This is the Makefile for the Lecture 22 Example.

CC := gcc
CFLAGS := -std=c11 -Wall

SIMD_OBJECTS := test_simd.o simd.o

simd: $(SIMD_OBJECTS)
	$(CC) $(CFLAGS) -o simd $(SIMD_OBJECTS)

test_simd.o: simd.c simd.h
	$(CC) $(CFLAGS) -c test_simd.c

simd.o: simd.c simd.h
	$(CC) $(CFLAGS) -c simd.c

executables := simd

all: $(executables)

clean:
	rm -rf *.o *.swp $(executables)
