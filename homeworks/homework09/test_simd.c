/***********************************************
 * File Name: test_simd.c
 * For use in the Homework 09 Assignment
 * This file may not be modified for any reason
 ***********************************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "simd.h"

#define SUCCESS 1
#define FAILURE 0

int main( const int argc, const char* argv[] ) {

	if (argc != 2 ){
		fprintf(stderr, "Must have ./simd [num_tests]\n");
		return EXIT_FAILURE;
	}
	
	/* Convert the input to the number of tests */
	int num_tests = atoi(argv[1]);
	int loop_tests;

	fprintf(stdout, "Let's generate a randomized array.\n");

	int vals[NUM_ELEMS];
	long long int reference;
	long long int simd;
	long long int simdu;
	int assignment_tests = SUCCESS;

	for (unsigned int i = 0; i < NUM_ELEMS; i++) 
		vals[i] = rand() % 256;

	fprintf(stdout, "Starting randomized sum.\n");

	/* Test reference using clock_t */
	clock_t start = clock();

	for(loop_tests = 0; loop_tests < num_tests; ++loop_tests)
		reference = sum(vals);

	clock_t end = clock();
	clock_t reft = end - start;

	/* Print the sum results */
	fprintf(stdout, "-------------------------\n");
	fprintf(stdout, "Sum: %lld\n", reference);
	fprintf(stdout, "Average Number of clocks: %lf\n", (double)reft/(double)num_tests);

	fprintf(stdout, "-------------------------\n");
	fprintf(stdout, "Starting randomized unrolled sum.\n");
	fprintf(stdout, "Sum: %lld\n", sum_unrolled(vals));

	fprintf(stdout, "-------------------------\n");
	fprintf(stdout, "Starting randomized SIMD sum.\n");
	start = clock();
	simd = sum_simd(vals);
	end = clock();
	clock_t simdt = end - start;

	fprintf(stdout, "Sum: %lld\n", simd);
	fprintf(stdout, "Number of clocks: %ld\n", simdt);

	if (simd != reference) {
		fprintf(stdout, "Test Failed! SIMD sum %lld doesn't match reference sum %lld!\n", simd, reference);
		assignment_tests = FAILURE;
	}
	
	if (reft <= simdt * 2) {
		fprintf(stdout, "Test Failed! SIMD sum provided less than 2X speedup.\n");
		assignment_tests = FAILURE;
	}

	fprintf(stdout, "-------------------------\n");
	fprintf(stdout, "Starting randomized SIMD unrolled sum.\n");
	start = clock();
	simdu = sum_simd_unrolled(vals);
	end = clock();
	clock_t simdut = end - start;

	fprintf(stdout, "Sum: %lld\n", simdu);
	fprintf(stdout, "Number of clocks: %ld\n", simdt);

	if (simdu != reference) {
		fprintf(stdout, "Test Failed! SIMD_UNROLLED sum %lld doesn't match reference sum %lld!\n", simdu, reference);
		assignment_tests = FAILURE;
	}

	if (simdt <= simdut) {
		fprintf(stdout, "Test Failed! SIMD unrolled function provided no speedup.\n");
		assignment_tests = FAILURE;
	}

	if (assignment_tests == SUCCESS) {
		fprintf(stdout, "All tests Passed! Correct values were produced, and speedups were achieved!\n");
		return EXIT_SUCCESS;
	} else {
		return EXIT_FAILURE;
	}

}
