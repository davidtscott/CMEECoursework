#include <stdio.h>
#include <stdbool.h>

int main (void)
{
    // The while loop 
    int i = 0;
    
    while (i < 10 && i != 0){
        printf("loop iteration: %i\n", i);
        ++i;
    } 

    i = 0;

    // do while loop 
    do {
        printf("do-while loop iteration: %i\n", i);
        ++i;
    } while (i < 10 && i != 0);
    
    for (i = 0 ; i < 10; i++){
        printf("for loop iteration: %i\n", i);
    }

    return 0;
}
