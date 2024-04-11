# Author: Prof. Matthew Morrison
# E-mail: matt.morrison@nd.edu
#
# This is the Makefile for the Lecture 23 Example.

# gcc is for the compiler for C
CC := gcc
CFLAGS := -std=c11
OMP := -fopenmp

executables := class_loop class_loop_seq hello hello_safe class_loop_parallel class_loop_parallel_fs class_loop_parallel_for

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
	$(CC) $(CFLAGS) $(OMP) -c hello.c

hello: hello.o
	$(CC) $(OMP) -o hello hello.o
	
	
# Create the Hello with Thread Safety Library
hello_safe.o: hello_safe.c
	$(CC) $(CFLAGS) $(OMP) -c hello_safe.c

hello_safe: hello_safe.o
	$(CC) $(OMP) -o hello_safe hello_safe.o
	
	
# Create the Class Loop Original - False Sharing
class_loop_parallel_fs.o: class_loop_parallel_fs.c
	$(CC) $(CFLAGS) $(OMP) -c class_loop_parallel_fs.c

class_loop_parallel_fs: class_loop_parallel_fs.o
	$(CC) $(OMP) -o class_loop_parallel_fs class_loop_parallel_fs.o


# Create the Class Loop with the parallel pragma
class_loop_parallel.o: class_loop_parallel.c
	$(CC) $(CFLAGS) $(OMP) -c class_loop_parallel.c

class_loop_parallel: class_loop_parallel.o
	$(CC) $(OMP) -o class_loop_parallel class_loop_parallel.o
	
	
# Create the Class Loop with the parallel and for pragmas
class_loop_parallel_for.o: class_loop_parallel_for.c
	$(CC) $(CFLAGS) $(OMP) -c class_loop_parallel_for.c

class_loop_parallel_for: class_loop_parallel_for.o
	$(CC) $(OMP) -o class_loop_parallel_for class_loop_parallel_for.o


# Test
loop_test: class_loop class_loop_seq class_loop_parallel class_loop_parallel_for
	./class_loop 1048576
	./class_loop_seq 1048576
	./class_loop_parallel 1048576
	./class_loop_parallel_for 1048576


# Make all
all: $(executables)

# Make clean
clean:
	rm -rf *.o *.swp $(executables)
