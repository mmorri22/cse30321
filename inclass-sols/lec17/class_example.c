#include <time.h>
#include <stdio.h>
#include <stdlib.h>

#define NUM_LOOPS 1000

typedef struct example{
	int int1;
	double double1;
	float float1;
	double double2;
	int int2;
}example;

int func( int count, example* the_arr, long unsigned int index ){
    return count += the_arr[index].int1;
}

int main( const int argc, const char* argv[] ){

	long unsigned int array_size = atoi( argv[1] );
	int sum = 0, num_times = 0;

	clock_t start_t = clock();

	for( num_times = 0 ; num_times < NUM_LOOPS; ++num_times ){

		example* the_list = (example *)calloc( array_size, sizeof(example) );
		
		int i;
		for(i = 0; i < array_size; ++i){
			the_list[i].int1 = i;
			the_list[i].double1 = (double)i;
			the_list[i].float1 = (float)i;
			the_list[i].double2 = (double)(i+1);
			the_list[i].int2 = i+1;
		}
			
		int test;
		for(test = 0; test < 4; ++test){
			
			long unsigned int index;
			for( index = 0; index < array_size; ++index ){
				
				the_list[index].int1 += func( test, the_list, index );
				sum += the_list[index].int2;
			}
		}
		
		free( the_list );

	}

	clock_t end_t = clock();

	double average_time = (double)(end_t - start_t)/(double)(CLOCKS_PER_SEC) ;

	fprintf( stdout, "Array Size: %ld\n", sizeof(example));
	fprintf( stdout, "Array Memory Consumed: %ld\n", array_size*sizeof(example));
	fprintf( stdout, "Num clocks: %ld\n", end_t - start_t );
	fprintf( stdout, "Avg clocks: %.6lfms\n", average_time / NUM_LOOPS * 1000 );

    return EXIT_SUCCESS;
}