#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define NMAX 50

/***************************
 * Function Name: fibonacci
 * Pre-Conditions: None
 * Post-Conditions: None
 *
 * Creates a dynamic array of NMAX size and
 * calculates the first NMAX fibonacci elements
 *******************************/
void fibonacci( );

int main(void) {

	/* Run 10,000,000 tests */
	long unsigned int num_tests = 10000000;

	/* clock_t is a type from #include <time.h> */
	/* clock_t is equivalent to a 64-bit signed integer */
	/* We start the profiling */
	clock_t time_start = clock();

	long unsigned int iter;
	for (iter = 0; iter < num_tests; ++iter)
		fibonacci();

	/* Obtain the end time and complete the time profile */
	clock_t time_end = clock();

	/* compute average execution time */
	double avg_clks = ((double)time_end - (double)time_start) / (double)CLOCKS_PER_SEC;

	/* print avg execution time in milliseconds */
	fprintf( stdout, "Start time : %ld\n", time_start );
	fprintf( stdout, "Finish time: %ld\n", time_end );
	fprintf( stdout, "Clocks per second: %ld\n", CLOCKS_PER_SEC );
	fprintf( stdout, "Average Clocks: %.3lfs\n", avg_clks );

	return 0;
}


void fibonacci( )
{

	/* An array of NMAX unsigned ints stored on the Heap */
	int* results_buffer = (int *)malloc( NMAX * sizeof(int) );

	/* First array element  */
	results_buffer[0] = 1;

	/* Second array element */
	results_buffer[1] = 1;

	long unsigned int iter;
	for (iter = 2; iter < NMAX; iter++) {

		results_buffer[ iter ] = results_buffer[ iter-2 ] + results_buffer[ iter - 1 ];

	}

	free( results_buffer );
}
