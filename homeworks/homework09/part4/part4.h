#ifndef PART4_H
#define PART4_H

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <x86intrin.h>

#define NUM_ELEMENTS 16394
#define OUTER_ITERATIONS 16384

long long int sum(int vals[NUM_ELEMENTS]);

long long int unrolled_sum(int vals[NUM_ELEMENTS]);

long long int simd_sum(int vals[NUM_ELEMENTS]);

long long int simd_unrolled_sum(int vals[NUM_ELEMENTS]);

#endif
