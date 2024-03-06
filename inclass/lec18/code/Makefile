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
dyn_no_opt:
	$(CC) dyn_no_opt.c -o dyn_no_opt

# Trace Executable and Run
dyn_cache_opt:
	$(CC) dyn_cache_opt.c -o dyn_cache_opt
	
# Trace Executable and Run
dyn_reg_opt:
	$(CC) dyn_reg_opt.c -o dyn_reg_opt

# Executable Names
loop1: loop1_no_opt loop1_cache_opt loop1_reg_opt

loop2: loop2_no_opt loop2_cache_opt loop2_reg_opt

dyn: dyn_no_opt dyn_cache_opt dyn_reg_opt
	./dyn_no_opt
	./dyn_cache_opt
	./dyn_reg_opt
	rm dyn_no_opt dyn_cache_opt dyn_reg_opt

executables := loop1_no_opt loop1_cache_opt loop1_reg_opt loop2_no_opt loop2_cache_opt loop2_reg_opt loop3 dyn_no_opt dyn_cache_opt dyn_reg_opt

# Make all
all: $(executables)

# Make clean
clean:
	rm -rf *.o *.swp $(executables)