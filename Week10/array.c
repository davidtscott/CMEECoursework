#include <stdio.h>

int main (void)
{
    int intarray[5];
    // type int 
    // name intarray
    // square brackets [] define array
    // 
    int intarray[arraylen];
    int implarray[ ] = { 1, 2, 4, 5, 6, 7};
    // implicit array with 6 elements 

    int i = 0;
    int x = 0;
    for (i = 0; i < 5; ++i) {
        x = intarray[i];
        printf("Value at intarray[%i] is: %i\n", i, x);
    }

    for (i = 0; i < 10; ++i) {
        x = implarray[i];
        printf("Value at implarray[%i] is: %i\n", i, x);
    }

    int joinedarray[arraylen + 6];

    for (i = 0; i < (arraylen + 6); ++i){
        if (i < arraylen) {
            joinedarray[i] = intarray[i];
        }

        joinedarray[i + arraylen] = implarray[i];
    }

    for (i = 0; i < (arraylen + 6); ++i){
        printf(" %i", joinedarray[i]);
    }
    printf("\n");

    return 0;
}
