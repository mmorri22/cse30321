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

    int block_size = (int)array_len / max_threads;

    clock_t start = clock();

    for( int loop = 0; loop < num_tests; ++loop ){

        #pragma omp parallel
        {

            /* Load from cache into registers reduces cache misses */
            int w_reg0 = w[0];
            int w_reg1 = w[1];
            int w_reg2 = w[2];
            int w_reg3 = w[3];
            int w_reg4 = w[4];

            int tid = omp_get_thread_num(); 

            for( int i = tid*block_size; i < array_len && (tid+1)*block_size - 1; ++i ){
                // Unroll loop reduces branch mispredictions
                int t = x[i]*w_reg0;   
                t += x[i+1]*w_reg1;
                t += x[i+2]*w_reg2;
                t += x[i+3]*w_reg3;
                t += x[i+4]*w_reg4;
                y[i] = t;   // Only perform one sw per loop
            }

        }
    }

    clock_t stop = clock();
    
    free(x);
    free(y);
    free(w);

    double elapsedTime = (double)(stop-start);

	fprintf( stdout, "Clocks for all loops   : %ld\n", (stop-start) / (clock_t)(max_threads) );
    fprintf( stdout, "Average clocks per loop: %0.3lf\n", elapsedTime / (double)(num_tests * max_threads));
    fprintf( stdout, "--------------------------------\n");


    return EXIT_SUCCESS;


}