#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

/****************************************************
 * For Homework 08 - Part 1
 * Modify using only register, array, or loop changes only
 * Do not implement any OpenMP methods in this loop
 ***************************************************/
void dgemm_seq( double** a, double** b, double** c, int N ){

	int iter, jter, kter;
	
	for( iter = 0; iter < N; ++iter ){

		for( jter = 0; jter < N; ++jter ){

			double cij = c[iter][jter];

			for( kter = 0; kter < N; ++kter ){
				cij += a[iter][kter] * b[kter][jter];
			}
			
			c[iter][jter] = cij;
		}
	}
}

/****************************************************
 * For Homework 08 - Part 3
 * Modify using only register or loop changes only
 * Do not implement any OpenMP methods in this loop
 ***************************************************/
void dgemm_parallel_no_blocking( double** a, double** b, double** c, int N, int num_threads ){

	
	#pragma omp parallel shared( a, b, c )
	{
		
		int iter, jter, kter;
		#pragma omp for schedule(static, 32768)
		for( iter = 0; iter < N; ++iter ){

			for( jter = 0; jter < N; ++jter ){

				double cij = c[iter][jter];

				for( kter = 0; kter < N; ++kter ){
					cij += a[iter][kter] * b[kter][jter];
				}
				
				c[iter][jter] = cij;
			}
		}
	}
}

void dgemm_parallel_blocking( double** a, double** b, double** c, int N, int num_threads ){

	int block_size = N / num_threads;
	
	#pragma omp parallel shared( a, b, c, block_size )
	{
		
		int iter, jter, kter;
		
		int tid = omp_get_thread_num();
		int start_index = tid * block_size;
		int end_index = ( (tid+1)*block_size - 1 < N ) ? (tid+1)*block_size - 1 : N - 1;

		
		#pragma omp for schedule(static, 32768)
		for( iter = start_index; iter < end_index; ++iter ){

			
			for( jter = start_index; jter < end_index; ++jter ){

				double cij = c[iter][jter];

				for( kter = start_index; kter < end_index; ++kter ){
					cij += a[iter][kter] * b[kter][jter];
				}
				
				c[iter][jter] = cij;
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

    srand( (unsigned int)time(0) );

    if(argc != 2){
		fprintf(stderr, "Requires two inputs ./dgemm_matrix [Size of Matrix\n" );
        return EXIT_FAILURE;
	}
	
	/**********************************************************************/
	/*************************** Modify Here ******************************/
	/* Change this line to get the maximum number of threads using OpenMP */
	/**********************************************************************/
    int num_threads = omp_get_max_threads();

	/**********************************************************************/
	/***************** Do not modify below this line **********************/
	/**********************************************************************/
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
		fprintf( stdout, "Test %d cycles = %lf\n", kter+1, (double)(stop_original-start_original) );
		
		no_improvement_total += (double)(stop_original-start_original);
    }

	/* Sequential Improvement Tests */
	double improvement_seq_total;

    for(int kter = 0; kter < num_tests; ++kter){
		fprintf( stdout, "Running Test with Sequential Improvement, Test %d\n", kter+1 );
		clock_t start_improvement_seq = clock();
        dgemm_seq( a, b, c_seq, (int)N );
		clock_t stop_improvement_seq = clock();
		fprintf( stdout, "Test %d cycles = %lf\n", kter+1, (double)(stop_improvement_seq-start_improvement_seq) );
		
		improvement_seq_total += (double)(stop_improvement_seq-start_improvement_seq);
    }
	
	/* Parallel Improvement with No Blocking Tests */
	double improvement_parallel_no_blocking_total;

    for(int kter = 0; kter < num_tests; ++kter){
		fprintf( stdout, "Running Test with Parallel - No Blocking Improvement, Test %d\n", kter+1 );
		clock_t start_improvement_pnb = clock();
        dgemm_parallel_no_blocking( a, b, c_no_blocking, (int)N, num_threads );
		clock_t stop_improvement_pnb = clock();
		fprintf( stdout, "Test %d cycles = %lf\n", kter+1, (double)(stop_improvement_pnb-start_improvement_pnb)/(double)(num_threads) );
		
		improvement_parallel_no_blocking_total += (double)(stop_improvement_pnb-start_improvement_pnb);
    }
	
	/* Parallel Improvement with Blocking Tests */
	double improvement_parallel_blocking_total;

    for(int kter = 0; kter < num_tests; ++kter){
		fprintf( stdout, "Running Test with Parallel - With Blocking Improvement, Test %d\n", kter+1 );
		clock_t start_improvement_pb = clock();
        dgemm_parallel_blocking( a, b, c_no_blocking, (int)N, num_threads );
		clock_t stop_improvement_pb = clock();
		fprintf( stdout, "Test %d cycles = %lf\n", kter+1, (double)(stop_improvement_pb-start_improvement_pb)/(double)(num_threads) );
		
		improvement_parallel_blocking_total += (double)(stop_improvement_pb-start_improvement_pb);
    }

	/****** Presentations of Final Test Results **********/

    fprintf( stdout, "--------------------------------\n");
	fprintf( stdout, "No Improvement Test\n" );
	fprintf( stdout, "Clocks for all tests   : %.3lf\n", no_improvement_total);
	fprintf( stdout, "Average clocks per test: %.3lf\n", no_improvement_total / (double)num_tests );    
    fprintf( stdout, "--------------------------------\n");
	
    fprintf( stdout, "--------------------------------\n");
	fprintf( stdout, "Sequential DGEMM Test\n" );
	fprintf( stdout, "Clocks for all tests   : %.3lf\n", improvement_seq_total);
	fprintf( stdout, "Average clocks per test: %.3lf\n", improvement_seq_total / (double)num_tests );    
    fprintf( stdout, "--------------------------------\n");

	fprintf( stdout, "Parallel DGEMM - No Blocking - Test\n" );
    fprintf( stdout, "Number of Threads: %d\n", num_threads);
	fprintf( stdout, "Clocks for all tests   : %.3lf\n", (improvement_parallel_no_blocking_total) / (double)(num_threads) );
    fprintf( stdout, "Average clocks per test: %.3lf\n", improvement_parallel_no_blocking_total / (double)(num_tests * num_threads));
	
    fprintf( stdout, "--------------------------------\n");
	fprintf( stdout, "Parallel DGEMM - Blocking - Test\n" );
    fprintf( stdout, "Number of Threads: %d\n", num_threads);
	fprintf( stdout, "Clocks for all tests   : %.3lf\n", (improvement_parallel_blocking_total) / (double)(num_threads) );
    fprintf( stdout, "Average clocks per test: %.3lf\n", improvement_parallel_blocking_total / (double)(num_tests * num_threads));
	
    fprintf( stdout, "--------------------------------\n");
	fprintf( stdout, "Comparisons: \n" );
	
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