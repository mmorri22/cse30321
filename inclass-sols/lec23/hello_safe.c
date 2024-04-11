#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main () {
    int x = 0; //Shared variable
	
	fprintf( stdout, "Total number of threads is %d\n",  omp_get_max_threads() );
	
	#pragma omp parallel
	{
		int tid = omp_get_thread_num(); 

		//Private variable - Create thread safe region
        #pragma omp critical
        {
			++x;
		}
		
		fprintf(stdout, "Hello World from thread %d, x = %d at %p\n", tid, x, &x );
		
		if(tid==0) {
            // Note the value of x that prints here will be the one that prints at the end
			fprintf(stdout, "Result of tid 0: x = %d\n", x );		
		}
	}	

    // 
	fprintf(stdout, "Done with parallel segment. x = %d\n", x);
	
	return EXIT_SUCCESS;
}
