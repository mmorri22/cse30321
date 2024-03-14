/***********************************************
 * File Name: test_part4.c
 * For use in the Homework 09 Assignment
 * This file may not be modified for any reason
 ***********************************************/

#include "part4.h"

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

	/* Create the randomized array */
	fprintf(stdout, "Generate a randomized array...");

	/* Seed the random number generator */
	srand( (unsigned int)time(0) );

	int vals[NUM_ELEMENTS];
	long long int reference;
	long long int simd;
	long long int simdu;
	int assignment_tests = SUCCESS;

	for (unsigned int i = 0; i < NUM_ELEMENTS; i++) 
		vals[i] = rand() % 256;

	fprintf( stdout, "... array generated.\n");

	/*********************************************************
	 * Calculating the reference randomized sum for the tests
	 *********************************************************/
	fprintf(stdout, "-------------------------\n");
	fprintf(stdout, "Calculating randomized sum - No modifications.\n");

	/* Test reference using clock_t */
	clock_t start = clock();

	for(loop_tests = 0; loop_tests < num_tests; ++loop_tests)
		reference = sum(vals);

	clock_t end = clock();
	clock_t reft = end - start;

	/* Print the sum results */
	fprintf(stdout, "Sum: %lld\n", reference);
	fprintf(stdout, "Average time: %.3lf\n", (double)reft/(double)(num_tests * CLOCKS_PER_SEC) );

	/*********************************************************
	 * Performing the unrolled result students will use as a reference
	 *********************************************************/

	fprintf(stdout, "-------------------------\n");
	fprintf(stdout, "Starting randomized unrolled sum.\n");
	long long int unrolled_sum_val;
	start = clock();

	for(loop_tests = 0; loop_tests < num_tests; ++loop_tests)
		unrolled_sum_val = unrolled_sum(vals);
	
	end = clock();

	clock_t rand_unrolled_t = end - start;

	fprintf(stdout, "Unrolled Sum: %lld\n", unrolled_sum_val);
	fprintf(stdout, "Average time: %.3lfs\n", (double)rand_unrolled_t/(double)(num_tests * CLOCKS_PER_SEC) );

	/*********************************************************
	 * Testing the student's SIMD sum example
	 *********************************************************/

	fprintf(stdout, "-------------------------\n");
	fprintf(stdout, "Starting randomized SIMD sum.\n");
	start = clock();

	for(loop_tests = 0; loop_tests < num_tests; ++loop_tests)
		simd = simd_sum(vals);
	
	end = clock();

	clock_t simdt = end - start;

	fprintf(stdout, "Sum: %lld\n", simd);
	fprintf(stdout, "Average time: %.3lfs\n", (double)simdt/(double)(num_tests * CLOCKS_PER_SEC) );

	if (simd != reference) {
		fprintf(stdout, "Test Failed! SIMD sum %lld doesn't match reference sum %lld!\n", simd, reference);
		assignment_tests = FAILURE;
	}
	
	if (reft <= simdt * 2) {
		fprintf(stdout, "Test Failed! SIMD sum provided less than 2X speedup.\n");
		assignment_tests = FAILURE;
	}

	/*********************************************************
	 * Testing the student's unrolled SIMD sum example
	 *********************************************************/

	fprintf(stdout, "-------------------------\n");
	fprintf(stdout, "Starting randomized SIMD unrolled sum.\n");
	start = clock();

	for(loop_tests = 0; loop_tests < num_tests; ++loop_tests)
		simdu = simd_unrolled_sum(vals);

	end = clock();
	clock_t simdut = end - start;

	fprintf(stdout, "Sum: %lld\n", simdu);
	fprintf(stdout, "Average time: %.3lfs\n", (double)simdut/(double)(num_tests * CLOCKS_PER_SEC) );

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
