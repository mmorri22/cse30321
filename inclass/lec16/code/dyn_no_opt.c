#include <time.h>
#include <stdlib.h>
#include <stdio.h>

#define NUM_LOOPS 1000

int  func( int count, long unsigned int  value ){
    return count += value;
}

int main( )
{
	int ARRAY_SIZE;
	fprintf(stdout, "Enter the size of the array: ");
	fscanf(stdin, "%d", &ARRAY_SIZE );

    int* arr = (int *)calloc(ARRAY_SIZE, sizeof(int));
	
	int num_times = 0;
	
	int sum = 0;
    
    clock_t start_t = clock();
	
	for( num_times = 0; num_times < NUM_LOOPS; ++num_times ){
		
		int count;
		for(count = 0; count < 5; ++count){
			
			long unsigned int idx;
			for( idx = 0; idx < ARRAY_SIZE; ++idx ){
				
				arr[idx] = func( count, arr[idx] );
				sum += arr[idx];
			}
		}
	
	}
    
    clock_t end_t = clock();
    
    double total_t = (double)(end_t - start_t) / (double)(CLOCKS_PER_SEC) * 1000;
    
    fprintf( stdout, "--------------------------------\n");
	fprintf( stdout, "Start = %ld, End = %ld\n", start_t, end_t );
    fprintf( stdout, "Array Size           : %d\n", ARRAY_SIZE);
	fprintf( stdout, "Number of loops      : %d\n", NUM_LOOPS);
	fprintf( stdout, "Clocks Per Second    : %ld\n", CLOCKS_PER_SEC );
    fprintf( stdout, "Clocks for all loops : %ld\n", end_t - start_t );
    fprintf( stdout, "Average time per loop: %.6lf ms\n", total_t  / NUM_LOOPS );
    fprintf( stdout, "--------------------------------\n");

	free(arr);

    return 0;
}