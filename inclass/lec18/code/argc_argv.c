#include <stdio.h>
#include <stdlib.h>


int main( int argc, char* argv[] ){

    int iter;
    for(iter = 0; iter < argc; ++iter){
        fprintf( stdout, "argv[%d] = %s\n", iter, argv[iter] );
    }

    return EXIT_SUCCESS;
}