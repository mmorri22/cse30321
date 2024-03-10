#!/bin/bash
# Author: Prof. Matthew Morrison
# E-mail: matt.morrison@nd.edu
#
# This is the Makefile for the Lecture 10 Example.

# gcc is for the compiler for C
CC := gcc
PP := g++

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

executables := dllist dllist_timed rbt_timed priority_timed top_down_splay

# Make all
all: $(executables)

# Make clean
clean:
	rm -rf *.o *.swp $(executables)