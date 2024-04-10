#ifndef OMP_APPS_H
#define OMP_APPS_H

#define _XOPEN_SOURCE   // Must include before #include's to perform drand48()
#include <math.h>
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define REPEAT 60
#define BUF_SIZE 8192

#define SIZE_T long unsigned int

#define ARRAY_SIZE 5000000

void v_add_naive(double* x, double* y, double* z);
void v_add_optimized_adjacent(double* x, double* y, double* z);
void v_add_optimized_chunks(double* x, double* y, double* z);
double dotp_naive(double* x, double* y, SIZE_T arr_size);
double dotp_manual_optimized(double* x, double* y, SIZE_T arr_size);
double dotp_reduction_optimized(double* x, double* y, SIZE_T arr_size);

double* gen_array(long unsigned int n);
int verify(double* x, double* y, void(*funct)(double *x, double *y, double *z));

#endif
