#include <time.h>
#include <stdio.h>

#define ARRAY_SIZE 16384

int func( int count, int value ){
    return count += value;
}

int main()
{
    int arr[ARRAY_SIZE];
    
    clock_t start_t = clock();
    
    int idx;
    for(idx = 0; idx < ARRAY_SIZE; ++idx){
        
        int count;
        for( count = 0; count < 5; ++count ){
            
            arr[idx] = func( count, arr[idx] );
            
        }
    }
    
    clock_t end_t = clock();
    
    double total_t = (double)(end_t - start_t) / (double)CLOCKS_PER_SEC;
    
    fprintf(stdout, "Total Clocks for Program  : %ld\n", end_t - start_t);
    fprintf(stdout, "Total time taken by CPU   : %lf\n", total_t  );

    return 0;
}