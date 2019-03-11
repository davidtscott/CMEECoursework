#include <stdio.h> 

int main (void)
{
    char mystring1[ ] = "This is a string";
    char string[ ] = {'A', ' ', 's', 't', 'r', 'i', 'n', 'g', '\0'};
    char five[ ] = "five"; // There are five characters i this string ut the '\0' is hidden 
    int i = 0;

    for (i = 0; mystring1[i]; ++i) {
        printf("%c", mystring1[i]); 

    }

    return 0; 
}


