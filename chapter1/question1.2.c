#include <stdio.h>

void reverse(char *);

void reverse(char *s)
{
    char *r = s;
    char t;
    if (s != NULL) {
        while (*++r) ;
        r--;
        while (s < r) {
            // Swap chars pointed by `str` and `r`
            t = *r;
            *r-- = *s;
            *s++ = t;
        }
    }
}


int main()
{
    char s[] = "abcdefg";
    reverse(s);
    printf("%s\n", s);
    return 0;
}
