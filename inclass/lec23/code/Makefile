# Author: Prof. Matthew Morrison
# E-mail: matt.morrison@nd.edu
#
# This is the Makefile for the Lecture 23 Example.

# gcc is for the compiler for C
CC := gcc
CFLAGS := -std=c11 -fopenmp
OMP := -fopenmp

executables := class_loop class_loop_seq hello class_loop_parallel dgemm_matrix dgemm_matrix_reg dgemm_matrix_parallel class_loop_parallel_fs

# Create the Class Loop Original
class_loop.o: class_loop.c
	$(CC) $(CFLAGS) -c class_loop.c

class_loop: class_loop.o
	$(CC) $(CFLAGS) -o class_loop class_loop.o


# Create the Class Loop Original
class_loop_seq.o: class_loop_seq.c
	$(CC) $(CFLAGS) -c class_loop_seq.c

class_loop_seq: class_loop_seq.o
	$(CC) $(CFLAGS) -o class_loop_seq class_loop_seq.o


# Create the Hello Library
hello.o: hello.c
	$(CC) $(CFLAGS) -c hello.c

hello: hello.o
	$(CC) $(OMP) -o hello hello.o
	
	
# Create the Class Loop Original
class_loop_parallel_fs.o: class_loop_parallel_fs.c
	$(CC) $(CFLAGS) -c class_loop_parallel_fs.c

class_loop_parallel_fs: class_loop_parallel_fs.o
	$(CC) $(OMP) -o class_loop_parallel_fs class_loop_parallel_fs.o


# Create the Class Loop Original
class_loop_parallel.o: class_loop_parallel.c
	$(CC) $(CFLAGS) -c class_loop_parallel.c

class_loop_parallel: class_loop_parallel.o
	$(CC) $(OMP) -o class_loop_parallel class_loop_parallel.o


# Test
loop_test: class_loop class_loop_seq class_loop_parallel
	./class_loop 1048576
	./class_loop_seq 1048576
	./class_loop_parallel 1048576


# Create the DGEMM Matrix Test
dgemm_matrix.o: dgemm_matrix.c
	$(CC) $(CFLAGS) -c dgemm_matrix.c

dgemm_matrix: dgemm_matrix.o
	$(CC) $(CFLAGS) -o dgemm_matrix dgemm_matrix.o


# Create the DGEMM Matrix Test with the Register Optimization
dgemm_matrix_reg.o: dgemm_matrix_reg.c
	$(CC) $(CFLAGS) -c dgemm_matrix_reg.c

dgemm_matrix_reg: dgemm_matrix_reg.o
	$(CC) $(CFLAGS) -o dgemm_matrix_reg dgemm_matrix_reg.o


# Create the DGEMM Matrix Test Parallel
dgemm_matrix_parallel.o: dgemm_matrix_parallel.c
	$(CC) $(CFLAGS) -c dgemm_matrix_parallel.c

dgemm_matrix_parallel: dgemm_matrix_parallel.o
	$(CC) $(OMP) -o dgemm_matrix_parallel dgemm_matrix_parallel.o

# DGEMM Matrix Test
dgemm_test: dgemm_matrix dgemm_matrix_reg dgemm_matrix_parallel
	./dgemm_matrix 1024
	./dgemm_matrix_reg 1024
	./dgemm_matrix_parallel 1024


# Make all
all: $(executables)

# Make clean
clean:
	rm -rf *.o *.swp $(executables)
