#include <stdio.h>

int main (void)
{
    int x = 0;

    x = x + 1;
    ++x; // add to x then evaluate 
    x++; // evaluate x then add to it 

    printf("The value of x: %i and %i\n", x++, x);


    return 0;

}