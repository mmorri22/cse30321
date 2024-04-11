# Author: Prof. Matthew Morrison
# E-mail: matt.morrison@nd.edu
#
# This is the Makefile for the Lecture 23 Example.

# gcc is for the compiler for C
CC := gcc
CFLAGS := -std=c11
OMP := -fopenmp

executables := dgemm_matrix dgemm_matrix_parallel

# Create the Class Loop Original
dgemm_matrix.o: dgemm_matrix.c
	$(CC) $(CFLAGS) -c dgemm_matrix.c

dgemm_matrix: dgemm_matrix.o
	$(CC) $(CFLAGS) -o dgemm_matrix dgemm_matrix.o


# Create the Class Loop Original
dgemm_matrix_parallel.o: dgemm_matrix_parallel.c
	$(CC) $(CFLAGS) -c dgemm_matrix_parallel.c

dgemm_matrix_parallel: dgemm_matrix_parallel.o
	$(CC) $(OMP) -o dgemm_matrix_parallel dgemm_matrix_parallel.o


# Test
dgemm_test: dgemm_matrix dgemm_matrix_parallel
	./dgemm_matrix 1024
	./dgemm_matrix_parallel 1024

# Make all
all: $(executables)

# Make clean
clean:
	rm -rf *.o *.swp $(executables)
