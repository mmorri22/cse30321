#!/bin/bash
# Author: Prof. Matthew Morrison
# E-mail: matt.morrison@nd.edu
#
# This is the Makefile for the Lecture 16 Example.

# gcc is for the compiler for C
CC := gcc
PP := g++

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
	rm -rf loop3


# Trace Executable and Run
dyn_no_opt:
	$(CC) dyn_no_opt.c -o dyn_no_opt

# Trace Executable and Run
dyn_cache_opt:
	$(CC) dyn_cache_opt.c -o dyn_cache_opt
	
# Trace Executable and Run
dyn_reg_opt:
	$(CC) dyn_reg_opt.c -o dyn_reg_opt

dyn_loop_unroll:
	$(CC) dyn_loop_unroll.c -o dyn_loop_unroll

dyn_inline:
	$(CC) dyn_inline.c -o dyn_inline

dyn_macro:
	$(CC) dyn_macro.c -o dyn_macro

# Executable Names
loop1: loop1_no_opt loop1_cache_opt loop1_reg_opt
	rm -rf loop1_no_opt loop1_cache_opt loop1_reg_opt

loop2: loop2_no_opt loop2_cache_opt loop2_reg_opt
	rm -rf loop1_no_opt loop1_cache_opt loop1_reg_opt

dyn: dyn_no_opt dyn_cache_opt dyn_reg_opt
	./dyn_no_opt
	./dyn_cache_opt
	./dyn_reg_opt
	rm dyn_no_opt dyn_cache_opt dyn_reg_opt

dyn_all: dyn_no_opt dyn_cache_opt dyn_reg_opt dyn_loop_unroll dyn_macro
	./dyn_no_opt
	./dyn_cache_opt
	./dyn_reg_opt
	./dyn_loop_unroll
	./dyn_macro
	rm dyn_no_opt dyn_cache_opt dyn_reg_opt dyn_loop_unroll dyn_macro

class_example:
	$(CC) class_example.c -o class_example

class_example_mod:
	$(CC) class_example_mod.c -o class_example_mod

class_example_sol:
	$(CC) class_example_sol.c -o class_example_sol

executables := loop1_no_opt loop1_cache_opt loop1_reg_opt loop2_no_opt loop2_cache_opt loop2_reg_opt loop3 dyn_no_opt dyn_cache_opt dyn_reg_opt dyn_inline dyn_loop_unroll dyn_macro class_example class_example_sol class_example_mod

# Make all
all: $(executables)

# Make clean
clean:
	rm -rf *.o *.swp $(executables)