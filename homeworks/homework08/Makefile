# Author: Prof. Matthew Morrison
# E-mail: matt.morrison@nd.edu
#
# This is the Makefile for Homework 09.

# gcc is for the compiler for C
CC := gcc
CFLAGS := -std=c11
OMP := -fopenmp -std=c11

executables := dgemm_matrix dgemm_matrix_parallel

# Create the Class Loop Original
dgemm_matrix.o: dgemm_matrix.c
	$(CC) $(OMP) -c dgemm_matrix.c

dgemm_matrix: dgemm_matrix.o
	$(CC) $(OMP) -o dgemm_matrix dgemm_matrix.o

# Test
test: dgemm_matrix
	./dgemm_matrix 512
	make clean

# Make all
all: $(executables)

# Make clean
clean:
	rm -rf *.o *.swp $(executables)
