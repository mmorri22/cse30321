#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

/****************************************************
 * For Homework 08:
 * You will only need to modify the contents of the dgemm function 
 * as well as the original Line 54 in main.
 * Otherwise, you will not need to modify the main function 
 ***************************************************/

void dgemm( double** a, double** b, double** c, int N, int num_threads ){

	int iter, jter, kter;
	
	for( iter = 0; iter < N; ++iter ){

		for( jter = 0; jter < N; ++jter ){

			for( kter = 0; kter < N; ++kter ){
				c[iter][jter] += a[iter][kter] * b[kter][jter];
			}
		}
	}
}

/* This is the original that will be benchmarked against the new program */
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
    int num_threads = 1;

	/* Do not modify below this line */
    long unsigned int N = (long unsigned int)atoi(argv[1]);

    double** a = (double**)calloc(N, sizeof(double*) );
    double** b = (double**)calloc(N, sizeof(double*) );
    double** c = (double**)calloc(N, sizeof(double*) );
	double** c_no_improvement = (double**)calloc(N, sizeof(double*) );

    long unsigned int iter, jter;
    for(iter = 0; iter < N; ++iter){
        a[iter] = (double *)calloc(N, sizeof(double) );
        b[iter] = (double *)calloc(N, sizeof(double) );
        c[iter] = (double *)calloc(N, sizeof(double) );

        for(jter = 0; jter < N; ++jter){
            a[iter][jter] = (double)(rand() % (int)N);
            b[iter][jter] = (double)(rand() % (int)N);
            c[iter][jter] = 0;
        }
    }
	
    clock_t start_original = clock();

    int num_tests = 5;
    for(int kter = 0; kter < num_tests; ++kter){
		fprintf( stdout, "Running Test with No Improvement, Test %d\n", kter+1 );
        dgemm_no_improvement( a, b, c, (int)N );
    }

    clock_t stop_original = clock();
	
    double elapsed_original = (double)(stop_original-start_original);

    clock_t start_improvement = clock();

    for(int kter = 0; kter < num_tests; ++kter){
		fprintf( stdout, "Running Test with Your Improvement, Test %d\n", kter+1 );
        dgemm( a, b, c, (int)N, num_threads );
    }

    clock_t stop_improvement = clock();

    double elapsed_improvement = (double)(stop_improvement-start_improvement);

    fprintf( stdout, "--------------------------------\n");
	fprintf( stdout, "Sequential DGEMM Test\n" );
	fprintf( stdout, "Clocks for all tests   : %.3lf\n", elapsed_original);
	fprintf( stdout, "Average clocks per test: %.3lf\n", elapsed_original / (double)num_tests );    
    fprintf( stdout, "--------------------------------\n");

	fprintf( stdout, "Parallel DGEMM Test\n" );
    fprintf( stdout, "Number of Threads: %d\n", num_threads);
	fprintf( stdout, "Clocks for all tests   : %.3lf\n", (elapsed_improvement) / (double)(num_threads) );
    fprintf( stdout, "Average clocks per test: %.3lf\n", elapsed_improvement / (double)(num_tests * num_threads));
    fprintf( stdout, "--------------------------------\n");
	fprintf( stdout, "Comparisons: \n" );
	int num_passes = 0;
	if( 1.5 * (elapsed_improvement) / (double)(num_threads) < elapsed_original ){
		fprintf( stdout, "PASSES sequential register improvement benchmark of 1.5x\n" );
		++num_passes;
	}
	else{
		fprintf( stdout, "FAILED sequential register improvement benchmark of 1.5x\n" );
	}
	
	if( 5* (elapsed_improvement) / (double)(num_threads) < elapsed_original ){
		fprintf( stdout, "PASSES omp parallel / no blocking improvement benchmark of 5x\n" );
		++num_passes;
	}
	else{
		fprintf( stdout, "FAILED omp parallel / no blocking improvement benchmark of 5x\n" );
	}
	
	if( 10 * (elapsed_improvement) / (double)(num_threads) < elapsed_original ){
		fprintf( stdout, "PASSES omp parallel with blocking improvement benchmark of 10x\n" );
		++num_passes;
	}
	else{
		fprintf( stdout, "FAILED omp parallel with blocking improvement benchmark of 10x\n" );
	}
	
	fprintf( stdout, "--------------------------------\n");
    
    for(iter = 0; iter < N; ++iter){
        free(a[iter]);
        free(b[iter]);
        free(c[iter]);
		free(c_no_improvement[iter]);
    }

    free(a);
    free(b);
    free(c);
	free(c_no_improvement);
    
    return EXIT_SUCCESS;
}