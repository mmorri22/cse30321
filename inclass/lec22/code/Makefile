# Author: Prof. Matthew Morrison
# E-mail: matt.morrison@nd.edu
#
# This is the Makefile for the Lecture 22 Example.

# gcc is for the compiler for C
CC := gcc
PP := g++
PY := python
PY3 := python3

# Trace Executable and Run
dgemm_matrix:
	$(CC) dgemm_matrix.c -o dgemm_matrix
	./dgemm_matrix
	$(PY) dgemm_matrix.py
	$(PY3) dgemm_matrix.py

dgemm_matrix_reg:
	$(CC) dgemm_matrix_reg.c -o dgemm_matrix_reg
	./dgemm_matrix_reg
	$(PY) dgemm_matrix_reg.py
	$(PY3) dgemm_matrix_reg.py


dgemm_matrix_large:
	$(CC) dgemm_matrix_large.c -o dgemm_matrix_large
	./dgemm_matrix_large 1024
	$(PY3) dgemm_matrix_large.py


executables := dgemm_matrix dgemm_matrix_reg dgemm_matrix_large

# Make all
all: $(executables)

# Make clean
clean:
	rm -rf *.o *.swp $(executables)