#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 4

void dgemm( double a[N][N], double b[N][N], double c[N][N]){

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

void print_result( double c[N][N] ){

    long unsigned int iter, jter;
    for( iter = 0; iter < N; ++iter ){
        fprintf( stdout, "[");
        for( jter = 0; jter < N; ++jter ){ 
            fprintf( stdout, " %2.0f" ,c[iter][jter] ); 
        }
        fprintf( stdout, " ]\n");
    }  
}

int main(){

    int num_tests = 1000;

    double a[N][N] = {{1,7,3,4},{2,1,8,5},{2,6,2,1},{4,3,4,7}};
    double b[N][N] = {{1,2,3,4},{5,6,7,8},{9,0,1,2},{3,4,5,6}};
    double c[N][N];

    clock_t start = clock();

    int iter;
    for(iter = 0; iter < num_tests; ++iter)
        dgemm( a, b, c );

    clock_t stop = clock();

    double elapsedTime = (double)(stop-start);

	fprintf( stdout, "Clocks Per Second        : %ld\n", CLOCKS_PER_SEC );
	fprintf( stdout, "Clocks for all multiply  : %ld\n", stop - start);
	fprintf( stdout, "Average time per multiply: %.6lf us\n", elapsedTime / (double)num_tests );    
    fprintf( stdout, "--------------------------------\n");


    return EXIT_SUCCESS;
}