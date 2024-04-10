#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

void dgemm( double** a, double** b, double** c, long unsigned int N ){

    #pragma omp parallel shared(a, b, c, N)
    {

        int iter, jter, kter;
		#pragma omp for private(iter, jter, kter) , 32768)
        for( iter = 0; iter < (int)N; ++iter ){

            for( jter = 0; jter < (int)N; ++jter ){

                // Register optimization
                double cij = c[iter][jter];
                for( kter = 0; kter < (int)N; ++kter ){
                    cij += a[iter][kter] * b[kter][jter];
                }

                // Register optimization
                c[iter][jter] = cij;
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

    int max_threads = omp_get_max_threads();

    clock_t start = clock();

    int num_tests = 5;
    for(int kter = 0; kter < num_tests; ++kter){
        dgemm( a, b, c, N );
    }

    clock_t stop = clock();

    double elapsedTime = (double)(stop-start);

	fprintf( stdout, "Parallel DGEMM Test\n" );
    fprintf( stdout, "Number of Threads: %d\n", max_threads);
	fprintf( stdout, "Clocks for all tests   : %ld\n", (stop-start) / (clock_t)(max_threads) );
    fprintf( stdout, "Average clocks per test: %0.3lf us\n", elapsedTime / (double)(num_tests * max_threads));
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