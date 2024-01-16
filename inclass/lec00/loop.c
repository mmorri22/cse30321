#include <stdio.h>

int main(){

    int i = 0;
    while( i < 1000000000){
        ++i;
    }
    fprintf(stdout, "%d\n", i);

    return 0;
}