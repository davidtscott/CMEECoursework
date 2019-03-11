#include <stdio.h> 

int add_integers(int a, int b)
{
    int result = 0;

    result = a + b;

    return result;

    // could also just do return a + b; and skip assignign to result variable 
}

int main (void)
{

    int a = 4;

    printf("Result: %i\n", add_integers(a, 2);

    return 0;
}

