#include <stdio.h> // standard io 

int main (void)
{
    
    int a = 7;
    float b = 2;
    float c = 0;

    c = a / b; /* can write it with or without white space either side of the operator 
                       e.g a/b or a / b */

    printf("The result of %i divided by %f is: %f.\n", a, b, c);
    
    return 0;
}