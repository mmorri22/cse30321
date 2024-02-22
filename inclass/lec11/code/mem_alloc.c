#include <stdio.h>
#include <stdlib.h>

int main(){
	
	int* array_1 = (int *)calloc(10, sizeof(int));
	
	int* array_2 = (int *)calloc(10, sizeof(int));
	
	fprintf( stdout, "--------------------------------------\n");
	fprintf( stdout, "array_1 DM location: %p\n", array_1);
	fprintf( stdout, "array_2 DM location: %p\n", array_2);
	fprintf( stdout, "--------------------------------------\n\n");
	
	long unsigned int iter;
	fprintf( stdout, "array_1 array locations:\n");
	for( iter = 0; iter < 10; ++iter ){
		fprintf( stdout, "array_1[%lu] location: %p\n", iter, &array_1[iter]);
	}
	fprintf( stdout, "--------------------------------------\n\n");
	
	fprintf( stdout, "array_2 array locations:\n");
	for( iter = 0; iter < 10; ++iter ){
		fprintf( stdout, "array_2[%lu] location: %p\n", iter, &array_2[iter]);
	}
	fprintf( stdout, "--------------------------------------\n");
	
	free(array_2);
	free(array_1);
	
	return 0;
	
}