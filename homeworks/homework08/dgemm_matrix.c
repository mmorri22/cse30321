#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

/****************************************************
 * For Homework 08 - Part 3.1
 * Modify using only register, array, or loop changes only
 * Do not implement any OpenMP methods in this loop
 ***************************************************/
void dgemm_seq( double** a, double** b, double** c, int N ){

	int iter, jter, kter;
	
	for( iter = 0; iter < (int)N; ++iter ){

		for( jter = 0; jter < (int)N; ++jter ){

			for( kter = 0; kter < (int)N; ++kter ){
				c[iter][jter] += a[iter][kter] * b[kter][jter];
			}
		}
	}
}

/****************************************************
 * For Homework 08 - Part 3.2
 * Use the OpenMP pragmas, but do not implement blocking
 * Make sure you change the first line of the main as indicated in the assignment
 ***************************************************/
void dgemm_parallel_no_blocking( double** a, double** b, double** c, int N, int num_threads ){

	
	int iter, jter, kter;
	
	for( iter = 0; iter < (int)N; ++iter ){

		for( jter = 0; jter < (int)N; ++jter ){

			for( kter = 0; kter < (int)N; ++kter ){
				c[iter][jter] += a[iter][kter] * b[kter][jter];
			}
		}
	}
}

/****************************************************
 * For Homework 08 - Part 3.3
 * Use the OpenMP pragmas, as well as blocking
 * Make sure you change the first line of the main as indicated in the assignment
 ***************************************************/
void dgemm_parallel_blocking( double** a, double** b, double** c, int N, int num_threads ){

	int iter, jter, kter;
	
	for( iter = 0; iter < (int)N; ++iter ){

		for( jter = 0; jter < (int)N; ++jter ){

			for( kter = 0; kter < (int)N; ++kter ){
				c[iter][jter] += a[iter][kter] * b[kter][jter];
			}
		}
	}
}

/* This is the original that will be benchmarked against the new program - Do not modify */
void dgemm_no_improvement( double** a, double** b, double** c, int N ){

	int iter, jter, kter;
	
	for( iter = 0; iter < (int)N; ++iter ){

		for( jter = 0; jter < (int)N; ++jter ){

			for( kter = 0; kter < (int)N; ++kter ){
				c[iter][jter] += a[iter][kter] * b[kter][jter];
			}
		}
	}
}

int main(const int argc, const char* argv[]){

	/**********************************************************************/
	/*************************** 3.2 Modify Here ******************************/
	/* Change this line to get the maximum number of threads using OpenMP */
	/**********************************************************************/
    int num_threads = 1;

	/**********************************************************************/
	/***************** Do not modify below this line **********************/
	/**********************************************************************/

    srand( (unsigned int)time(0) );

    if(argc != 2){
		fprintf(stderr, "Requires two inputs ./dgemm_matrix [Size of Matrix\n" );
        return EXIT_FAILURE;
	}
	
    long unsigned int N = (long unsigned int)atoi(argv[1]);

    double** a = (double**)calloc(N, sizeof(double*) );
    double** b = (double**)calloc(N, sizeof(double*) );
    double** c_seq = (double**)calloc(N, sizeof(double*) );
	double** c_no_blocking = (double**)calloc(N, sizeof(double*) );
	double** c_blocking = (double**)calloc(N, sizeof(double*) );
	double** c_no_improvement = (double**)calloc(N, sizeof(double*) );

    long unsigned int iter, jter;
    for(iter = 0; iter < N; ++iter){
        a[iter] = (double *)calloc(N, sizeof(double) );
        b[iter] = (double *)calloc(N, sizeof(double) );
        c_seq[iter] = (double *)calloc(N, sizeof(double) );
		c_no_blocking[iter] = (double *)calloc(N, sizeof(double) );
		c_blocking[iter] = (double *)calloc(N, sizeof(double) );
		c_no_improvement[iter] = (double *)calloc(N, sizeof(double) );

        for(jter = 0; jter < N; ++jter){
            a[iter][jter] = (double)(rand() % (int)N);
            b[iter][jter] = (double)(rand() % (int)N);
            c_seq[iter][jter] = 0;
			c_no_blocking[iter][jter] = 0;
			c_blocking[iter][jter] = 0;
			c_no_improvement[iter][jter] = 0;
        }
    }
	
	/* No Improvement Test */
	double no_improvement_total;

    int num_tests = 5;
    for(int kter = 0; kter < num_tests; ++kter){
		fprintf( stdout, "Running Test with No Improvement, Test %d\n", kter+1 );
		clock_t start_original = clock();
        dgemm_no_improvement( a, b, c_no_improvement, (int)N );
		clock_t stop_original = clock();
		
		no_improvement_total += (double)(stop_original-start_original);
    }

	/* Sequential Improvement Tests */
	double improvement_seq_total;

    for(int kter = 0; kter < num_tests; ++kter){
		fprintf( stdout, "Running Test with Sequential Improvement, Test %d\n", kter+1 );
		clock_t start_improvement_seq = clock();
        dgemm_seq( a, b, c_seq, (int)N );
		clock_t stop_improvement_seq = clock();
		
		improvement_seq_total += (double)(stop_improvement_seq-start_improvement_seq);
    }
	
	/* Parallel Improvement with No Blocking Tests */
	double improvement_parallel_no_blocking_total;

    for(int kter = 0; kter < num_tests; ++kter){
		fprintf( stdout, "Running Test with Parallel - No Blocking Improvement, Test %d\n", kter+1 );
		clock_t start_improvement_pnb = clock();
        dgemm_parallel_no_blocking( a, b, c_no_blocking, (int)N, num_threads );
		clock_t stop_improvement_pnb = clock();
		
		improvement_parallel_no_blocking_total += (double)(stop_improvement_pnb-start_improvement_pnb);
    }
	
	/* Parallel Improvement with Blocking Tests */
	double improvement_parallel_blocking_total;

    for(int kter = 0; kter < num_tests; ++kter){
		fprintf( stdout, "Running Test with Parallel - With Blocking Improvement, Test %d\n", kter+1 );
		clock_t start_improvement_pb = clock();
        dgemm_parallel_blocking( a, b, c_no_blocking, (int)N, num_threads );
		clock_t stop_improvement_pb = clock();
		
		improvement_parallel_blocking_total += (double)(stop_improvement_pb-start_improvement_pb);
    }

	/****** Presentations of Final Test Results **********/
	fprintf( stdout, "\nComparisons: \n" );
	
	int num_passes = 0;
	if( 1.5 * improvement_seq_total / (double)num_tests < no_improvement_total / (double)num_tests ){
		fprintf( stdout, "PASSES sequential register improvement benchmark of 1.5x\n" );
		++num_passes;
	}
	else{
		fprintf( stdout, "FAILED sequential register improvement benchmark of 1.5x\n" );
	}
	
	if( 34 * (improvement_parallel_no_blocking_total) / (double)(num_threads*num_tests) < no_improvement_total / (double)num_tests ){
		fprintf( stdout, "PASSES omp parallel / no blocking improvement benchmark of 34x\n" );
		++num_passes;
	}
	else{
		fprintf( stdout, "FAILED omp parallel / no blocking improvement benchmark of 34x\n" );
	}
	
	if( 150 * (improvement_parallel_blocking_total) / (double)(num_threads*num_tests) < no_improvement_total / (double)num_tests ){
		fprintf( stdout, "PASSES omp parallel with blocking improvement benchmark of 150x\n\n" );
		++num_passes;
	}
	else{
		fprintf( stdout, "FAILED omp parallel with blocking improvement benchmark of 150x\n\n" );
	}
	
	fprintf( stdout, "PASSES %d/3 TESTS\n", num_passes );
	
	fprintf( stdout, "--------------------------------\n");
    
    for(iter = 0; iter < N; ++iter){
        free(a[iter]);
        free(b[iter]);
        free(c_seq[iter]);
		free(c_no_improvement[iter]);
		free(c_no_blocking[iter]);
		free(c_blocking[iter]);
    }

    free(a);
    free(b);
    free(c_seq);
	free(c_no_improvement);
	free(c_no_blocking);
	free(c_blocking);
    
    return EXIT_SUCCESS;
}