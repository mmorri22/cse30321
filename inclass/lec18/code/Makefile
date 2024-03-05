#!/bin/bash
# Author: Prof. Matthew Morrison
# E-mail: matt.morrison@nd.edu
#
# This is the Makefile for the Lecture 10 Example.

# gcc is for the compiler for C
CC := gcc

# Trace Executable and Run
loop1_no_opt:
	$(CC) loop1_no_opt.c -o loop1_no_opt
	./loop1_no_opt

# Trace Executable and Run
loop1_cache_opt:
	$(CC) loop1_cache_opt.c -o loop1_cache_opt
	./loop1_cache_opt
	
# Trace Executable and Run
loop1_reg_opt:
	$(CC) loop1_reg_opt.c -o loop1_reg_opt
	./loop1_reg_opt


# Trace Executable and Run
loop2_no_opt:
	$(CC) loop2_no_opt.c -o loop2_no_opt
	./loop2_no_opt

# Trace Executable and Run
loop2_cache_opt:
	$(CC) loop2_cache_opt.c -o loop2_cache_opt
	./loop2_cache_opt
	
# Trace Executable and Run
loop2_reg_opt:
	$(CC) loop2_reg_opt.c -o loop2_reg_opt
	./loop2_reg_opt

# Trace Executable and Run
loop3:
	$(CC) loop3.c -o loop3
	./loop3
	$(info ************ This segmentation fault is deliberate ************)
	rm loop3

# Trace Executable and Run
loop4_no_opt:
	$(CC) loop4_no_opt.c -o loop4_no_opt

# Trace Executable and Run
loop4_cache_opt:
	$(CC) loop4_cache_opt.c -o loop4_cache_opt
	
# Trace Executable and Run
loop4_reg_opt:
	$(CC) loop4_reg_opt.c -o loop4_reg_opt

# Executable Names
loop1: loop1_no_opt loop1_cache_opt loop1_reg_opt

loop2: loop2_no_opt loop2_cache_opt loop2_reg_opt

loop4: 
	@read -p "Enter size of array : " ARRAY_SIZE; /
	@echo "Entered size =" $$ARRAY_SIZE; /

executables := loop1_no_opt loop1_cache_opt loop1_reg_opt loop2_no_opt loop2_cache_opt loop2_reg_opt loop3 loop4_no_opt loop4_cache_opt loop4_reg_opt

# Make all
all: $(executables)

# Make clean
clean:
	rm -rf *.o *.swp $(executables)