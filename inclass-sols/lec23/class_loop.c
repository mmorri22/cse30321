#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define WSIZE 5

int main( const int argc, const char* argv[] ){

    if( argc != 2){
        fprintf( stderr, "Need two inputs\n");
        return EXIT_FAILURE;
    }

    long unsigned int array_len = (long unsigned int)atoi(argv[1]);

    int* x = (int *)calloc(array_len + WSIZE, sizeof(int));
    int* y = (int *)calloc(array_len, sizeof(int));
    int* w = (int *)calloc(WSIZE, sizeof(int));

    int num_tests = 1000;

    clock_t start = clock();

    for( int loop = 0; loop < num_tests; ++loop ){
        for( long unsigned int i = 0; i < array_len; ++i ){
            int t = 0;
            for( long unsigned int j = 0; j < WSIZE; ++j ){
                t += x[i+j]*w[j];
                y[i] = t;
            }
        }
    }

    clock_t stop = clock();
    
    free(x);
    free(y);
    free(w);

    double elapsedTime = (double)(stop-start);

	fprintf( stdout, "Clocks for all loops   : %ld\n", stop-start);
    fprintf( stdout, "Average clocks per loop: %0.3lf\n", elapsedTime / (double)(num_tests));
    fprintf( stdout, "--------------------------------\n");


    return EXIT_SUCCESS;
}