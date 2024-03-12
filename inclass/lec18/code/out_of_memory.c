#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main( const int argc, const char* argv[] ){

    /* Remember the Year 2037 Problem - Why I must cast to unsigned int */
    srand( (unsigned int)time(0) );

    long unsigned int array_size = 1024 * 1024 * 1024;
    long unsigned int total_bytes = 0;

    while(1){

        char* char_array = (char *)calloc(array_size, sizeof(char) );
        total_bytes += array_size;

        /* Dr. Morrison's Golden Rule of Pointers */
        if( char_array == NULL ){

            /* But we'll see that we never actually get in here... */
            fprintf( stderr, "Failed to allocate %ld bytes \n", array_size );
            return EXIT_FAILURE;
        }
        else{
            fprintf( stdout, "Allocated %ld bytes of memory!\n", total_bytes );
        }

        // Whoops, forgot to free!

        /* Increase for the next array to be 1024 larger */
        array_size += 1024;

    }

    return EXIT_SUCCESS;
}