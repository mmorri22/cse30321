# Author: Matthew Morrison
# E-mail: matt.morrison@nd.edu
#
# This is the Makefile for the CSE 30321 Example

# CC is for the GCC compiler for C 
CC := gcc

# CFLAGS are the compiler flages for when we compile C code in this course 
CFLAGS := -O2 -g -std=c11 -Wall -Wextra -Wshadow -Wconversion -Werror 
	

# Command: make mem_alloc
mem_alloc: mem_alloc.o 
	$(CC) -o mem_alloc mem_alloc.o

mem_alloc.o: mem_alloc.c 
	$(CC) -c mem_alloc.c


# Command: make mem_alloc_pqc 
mem_alloc_pqc: mem_alloc_pqc.o 
	$(CC) $(CFLAGS) -o mem_alloc_pqc mem_alloc_pqc.o

mem_alloc_pqc.o: mem_alloc.c 
	$(CC) $(CFLAGS) -c mem_alloc.c -o $@
	
	
# Command: make dllist 
dllist: dllist.o 
	$(CC) -o dllist dllist.o

dllist.o: dllist.c 
	$(CC) -c dllist.c


# Command: make mem_alloc_pqc 
dllist_pqc: dllist_pqc.o 
	$(CC) $(CFLAGS) -o dllist_pqc dllist_pqc.o

dllist_pqc.o: dllist.c 
	$(CC) $(CFLAGS) -c dllist.c -o $@


executables := mem_alloc mem_alloc_pqc dllist dllist_pqc

# Make all (intPtrBad not include because of deliberate compiler errors) 
all: $(executables)

# Make clean
clean :
	rm -rf *.o $(executables)



