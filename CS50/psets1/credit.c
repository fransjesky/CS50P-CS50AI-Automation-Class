#include <cs50.h>
#include <stdio.h>

void multiplier(int digit);
void addition(int digit);

// variables init
int counter = 0;
int multiplier_sum = 0;
int addition_sum = 0;
int sum = 0;
int pattern_num = 0;

int main(void)
{
    // get user card number
    long card_number = get_long("Number: ");
    long temp_card_number = card_number;

    // loop through the card number to do the sum
    while (card_number > 0)
    {
        // get the pattern number to define the card type
        if (card_number < 99 && card_number > 9)
        {
            pattern_num = card_number;
        }

        if (counter % 2 > 0)
        {
            // multiply the digit
            multiplier(card_number % 10);
        }
        else
        {
            // sum the digit
            addition(card_number % 10);
        }
        counter++;
        card_number /= 10;
    }

    sum += multiplier_sum + addition_sum;

    if (sum % 10 == 0 && counter > 12 && counter < 17)
    {
        if (pattern_num == 22 || pattern_num == 51 || pattern_num == 55)
        {
            printf("MASTERCARD\n");
        }
        else if (pattern_num == 40 || pattern_num == 41 || pattern_num == 42 || pattern_num == 49)
        {
            printf("VISA\n");
        }
        else if (pattern_num == 37)
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

void multiplier(int digit)
{
    int multiply = digit * 2;

    if (multiply > 9)
    {
        while (multiply > 0)
        {
            multiplier_sum += multiply % 10;
            multiply /= 10;
        }
    }
    else
    {
        multiplier_sum += multiply;
    }
}

void addition(int digit)
{
    addition_sum += digit;
}
