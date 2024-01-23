#include <stdio.h>
#include <stdlib.h>

// Write the updated example struct
typedef struct first_struct{
    char* char_array;
    double first_double;
    double second_double;
    float first_float;
    float second_float;
    float third_float;
    int first_int;
    char first_char;
    char second_char;
    char third_char;
}first_struct;

int main(){

    first_struct* example_struct = (first_struct*)malloc( sizeof(first_struct) );

    size_t optimal_size = 3*sizeof(float) + 2*sizeof(double) + 3*sizeof(char) + sizeof(int) + sizeof(char *);
    fprintf( stdout, "Size of optimal first_struct = %lu\n", optimal_size );
    fprintf( stdout, "Size of first_struct = %lu\n", sizeof(first_struct) );

    fprintf( stdout, "The locations:\n");
    fprintf( stdout, "Base address  : %p\n", example_struct);
    fprintf( stdout, "char_array    : %p\n", &example_struct->char_array);
    fprintf( stdout, "first_double  : %p\n", &example_struct->first_double);
    fprintf( stdout, "second_double : %p\n", &example_struct->second_double);
    fprintf( stdout, "first_float   : %p\n", &example_struct->first_float);
    fprintf( stdout, "second_float  : %p\n", &example_struct->second_float);
    fprintf( stdout, "third_float   : %p\n", &example_struct->third_float);
    fprintf( stdout, "first_int     : %p\n", &example_struct->first_int);
    fprintf( stdout, "first_char    : %p\n", &example_struct->first_char);
    fprintf( stdout, "second_char   : %p\n", &example_struct->second_char);
    fprintf( stdout, "third_char    : %p\n", &example_struct->third_char);

    free(example_struct->char_array);
    free(example_struct);

    return EXIT_SUCCESS;
}