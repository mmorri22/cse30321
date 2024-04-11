#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void dgemm( double** a, double** b, double** c, long unsigned int N){

    long unsigned int iter, jter, kter;
    for( iter = 0; iter < N; ++iter ){
        for( jter = 0; jter < N; ++jter ){

            for( kter = 0; kter < N; ++kter ){
                c[iter][jter] += a[iter][kter] * b[kter][jter];
            }

        }
    }
}

int main(const int argc, const char* argv[]){

    srand( (unsigned int)time(0) );

    if(argc != 2)
        return EXIT_FAILURE;

    long unsigned int N = (long unsigned int)atoi(argv[1]);

    double** a = (double**)calloc(N, sizeof(double*) );
    double** b = (double**)calloc(N, sizeof(double*) );
    double** c = (double**)calloc(N, sizeof(double*) );

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

    clock_t start = clock();

    long unsigned int num_tests = 5;
    for(iter = 0; iter < num_tests; ++iter){
        dgemm( a, b, c, N );
    }

    clock_t stop = clock();

    double elapsedTime = (double)(stop-start);

    fprintf( stdout, "DGEMM Test\n" );
	fprintf( stdout, "Clocks for all tests   : %ld\n", stop - start);
	fprintf( stdout, "Average clocks per test: %.3lf us\n", elapsedTime / (double)num_tests );    
    fprintf( stdout, "--------------------------------\n");

    
    for(iter = 0; iter < N; ++iter){
        free(a[iter]);
        free(b[iter]);
        free(c[iter]);
    }

    free(a);
    free(b);
    free(c);
    
    return EXIT_SUCCESS;
}