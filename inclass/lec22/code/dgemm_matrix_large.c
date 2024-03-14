#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void dgemm( double** a, double** b, double** c, long unsigned int N){

    long unsigned int iter, jter, kter;
    for( iter = 0; iter < N; ++iter ){
        for( jter = 0; jter < N; ++jter ){

            // Register optimization
            double cij = c[iter][jter];

            for( kter = 0; kter < N; ++kter ){
                cij += a[iter][kter] * b[kter][jter];
            }

            // Register optimization
            c[iter][jter] = cij;
        }
    }
}

void print_result( double** c, long unsigned int N ){

    long unsigned int iter, jter;
    for( iter = 0; iter < N; ++iter ){
        fprintf( stdout, "[");
        for( jter = 0; jter < N; ++jter ){ 
            fprintf( stdout, " %2.0f" ,c[iter][jter] ); 
        }
        fprintf( stdout, " ]\n");
    }  
}

int main(const int argc, const char* argv[]){

    srand( (unsigned int)time(0) );

    if(argc != 2)
        return EXIT_FAILURE;

    long unsigned int N = atoi(argv[1]);

    double** a = (double**)calloc(N, sizeof(double*) );
    double** b = (double**)calloc(N, sizeof(double*) );
    double** c = (double**)calloc(N, sizeof(double*) );

    long unsigned int iter, jter;
    for(iter = 0; iter < N; ++iter){
        a[iter] = (double *)calloc(N, sizeof(double) );
        b[iter] = (double *)calloc(N, sizeof(double) );
        c[iter] = (double *)calloc(N, sizeof(double) );

        for(jter = 0; jter < N; ++jter){
            a[iter][jter] = (double)(rand() % N);
            b[iter][jter] = (double)(rand() % N);
            c[iter][jter] = 0;
        }
    }

    clock_t start = clock();

    long unsigned int num_tests = 5;
    for(iter = 0; iter < num_tests; ++iter){
        fprintf(stdout, "Test %ld\n", iter+1);
        dgemm( a, b, c, N );
    }

    clock_t stop = clock();

    double elapsedTime = (double)(stop-start);

	fprintf( stdout, "Clocks Per Second        : %ld\n", CLOCKS_PER_SEC );
	fprintf( stdout, "Clocks for all multiply  : %ld\n", stop - start);
	fprintf( stdout, "Average time per multiply: %.6lf us\n", elapsedTime / (double)num_tests );    
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