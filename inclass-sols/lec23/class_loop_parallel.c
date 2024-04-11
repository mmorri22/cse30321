#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

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
    int max_threads = omp_get_max_threads();
	
	clock_t start = clock();

    for( int loop = 0; loop < num_tests; ++loop ){
			
        /* Load from cache into registers reduces cache misses */
        int w_reg0 = w[0];
        int w_reg1 = w[1];
        int w_reg2 = w[2];
        int w_reg3 = w[3];
        int w_reg4 = w[4];

        int iter;

        for( iter = 0; iter < array_len; ++iter ){
            // Unroll loop reduces branch mispredictions
            int t = x[iter]*w_reg0;   
            t += x[iter+1]*w_reg1;
            t += x[iter+2]*w_reg2;
            t += x[iter+3]*w_reg3;
            t += x[iter+4]*w_reg4;
            y[iter] = t;   // Only perform one sw per loop
            
        }
    }

    clock_t stop = clock();
    clock_t elapsedTime = stop - start;
	
    free(x);
    free(y);
    free(w);

	fprintf( stdout, "Clocks for all loops   : %ld\n", elapsedTime / (clock_t)(max_threads) );
    fprintf( stdout, "Average clocks per loop: %0.3lf\n", (double) elapsedTime / (double)(num_tests * max_threads));
    fprintf( stdout, "--------------------------------\n");


    return EXIT_SUCCESS;


}