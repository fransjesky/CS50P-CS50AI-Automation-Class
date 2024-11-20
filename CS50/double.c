#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int value = 1;
    int length = get_int("What is the length of your array? ");
    int doubling[length];

    for (int i = 1; i <= length; i++)
    {
        doubling[i] = value;
        value *= 2;
        printf("%i\n", doubling[i]);
    }

    return 0;
}
