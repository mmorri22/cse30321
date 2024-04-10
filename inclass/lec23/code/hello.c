#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main () {
    int x = 0; //Shared variable	
	#pragma omp parallel
	{
		int tid = omp_get_thread_num(); 

		//Private variable - Whatever x is *at that moment* will add
		++x;
		
		fprintf(stdout, "Hello World from thread %d, x = %d at %p\n", tid, x, &x);
		
		if(tid==0) {
            // Note the value of x that prints here will be the one that prints at the end
			fprintf(stdout, "Number of threads = %d, x = %d\n", omp_get_num_threads(), x);		
		}
	}	

    // 
	fprintf(stdout, "Done with parallel segment. x = %d\n", x);
	
	return EXIT_SUCCESS;
}
