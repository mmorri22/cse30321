#!/bin/bash
# Author: Prof. Matthew Morrison
# E-mail: matt.morrison@nd.edu
#
# This is the Makefile for the Lecture 10 Example.

# gcc is for the compiler for C
CC := gcc
PP := g++

class_example:
	$(CC) class_example.c -o class_example

class_example_mod:
	$(CC) class_example_mod.c -o class_example_mod

class_example_sol:
	$(CC) class_example_sol.c -o class_example_sol

dllist:
	$(CC) dllist.c -o dllist

dllist_timed:
	$(CC) dllist_timed.c -o dllist_timed

top_down_splay:
	$(CC) top_down_splay.c -o top_down_splay

rbt_timed:
	$(PP) -std=c++2a rbt_timed.cpp -o rbt_timed

priority_timed:
	$(PP) -std=c++2a priority_timed.cpp -o priority_timed

executables := class_example class_example_sol class_example_mod dllist dllist_timed rbt_timed priority_timed top_down_splay

# Make all
all: $(executables)

# Make clean
clean:
	rm -rf *.o *.swp $(executables)