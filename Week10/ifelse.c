#include <stdio.h>
#include <stdbool.h>

int main (void)
{
    bool x = false;
    
    if (x == true) {
        // code executes in here 
        printf("x is non-zero\n");
    }
    else if (x == false) {
        printf("x is zero\n");
    }

    return 0;

}
