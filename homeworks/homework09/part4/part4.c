#include "part4.h"

long long int sum(int vals[NUM_ELEMENTS]) {

	long long int sum = 0;
	for(unsigned int w = 0; w < OUTER_ITERATIONS; w++) {
		for(unsigned int i = 0; i < NUM_ELEMENTS; i++) {
			if(vals[i] >= 128) {
				sum += vals[i];
			}
		}
	}

	return sum;
}

long long int unrolled_sum(int vals[NUM_ELEMENTS]) {

	long long int sum = 0;

	for(unsigned int w = 0; w < OUTER_ITERATIONS; w++) {
		for(unsigned int i = 0; i < NUM_ELEMENTS / 4 * 4; i += 4) {
			if(vals[i] >= 128) 
				sum += vals[i];

			if(vals[i + 1] >= 128) 
				sum += vals[i + 1];

			if(vals[i + 2] >= 128) 
				sum += vals[i + 2];
			
			if(vals[i + 3] >= 128) 
				sum += vals[i + 3];
		}

		/* Known as the "Tail Case" */
		/* For the 0-2 elements if NUM_ELEMENTS is not divisible by 4 */
		for(unsigned int i = NUM_ELEMENTS / 4 * 4; i < NUM_ELEMENTS; i++) {
			if (vals[i] >= 128) {
				sum += vals[i];
			}
		}
	}
	return sum;
}

long long int simd_sum(int vals[NUM_ELEMENTS]) {
	
	// DO NOT MODIFY THESE TWO VARIABLES FOR ANY REASON
	__m128i _127 = _mm_set1_epi32(127);		/* Empty vector with 127 numbers */
	long long int result = 0;				/* Result Sum variable */
	// DO NOT MODIFY THESE TWO VARIABLES FOR ANY REASON
	
	for(unsigned int w = 0; w < OUTER_ITERATIONS; w++) {
		/* YOUR CODE GOES HERE */

		/* You'll need a tail case. */

	}

	return result;
}

long long int simd_unrolled_sum(int vals[NUM_ELEMENTS]) {
	clock_t start = clock();
	__m128i _127 = _mm_set1_epi32(127);
	long long int result = 0;
	for(unsigned int w = 0; w < OUTER_ITERATIONS; w++) {
		/* COPY AND PASTE YOUR sum_simd() HERE */
		/* MODIFY IT BY UNROLLING IT */

		/* You'll need 1 or maybe 2 tail cases here. */

	}
	clock_t end = clock();
	printf("Time taken: %Lf s\n", (long double)(end - start) / CLOCKS_PER_SEC);
	return result;
}