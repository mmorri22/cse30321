#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main () {
    int x = 0; //Shared variable	
	#pragma omp parallel
	{
		int tid = omp_get_thread_num(); 
		//Private variable
		x++;
		
		fprintf(stdout, "Hello World from thread %d, x = %d\n", tid, x);
		
		if(tid==0) {
			fprintf(stdout, "Number of threads = %d\n", omp_get_num_threads());		
		}
	}	
	fprintf(stdout, "Done with parallel segment\n");
	
	return EXIT_SUCCESS;
}
