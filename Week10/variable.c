#include <stdio.h>

int main (void) 
{
    //int x; // define variable type
    //x = 1; // define variable 
    // can also declare on the sameline e.g int x = 0, y = 1, z = 2; etc 
    // it is less readible and more error prone. should declare on new lines. 

    //int x = 1;
    //int y = 1;
    //int z = 2;
    //x = 0;

    float y = 2.03;
    int x = 1;

    x = x + y;

    //assigning the addition of a int and a float to an int variable will only return int

    // other data types: 
    // char (character)
    // flt (float)
    // double (dbl)
    //_Bool (boolean)

    


    // can also give variables names such as int _AnInteger 
    //      can sensitive. alphanumeric characters adn underscores 
    // no dashes as they are part of character set used by C

    printf("The value of x: %i\n", x);
    // %i specifies format as int

    // never use global variables 
    // variable is changable data 

    return 0;
}

