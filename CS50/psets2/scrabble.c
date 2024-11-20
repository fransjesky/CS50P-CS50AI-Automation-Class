#include <cs50.h>
#include <stdio.h>
#include <string.h>

int char_checker(char letter);

int main(void)
{
    // get user input
    string word_1 = get_string("Player 1: ");
    string word_2 = get_string("Player 2: ");

    int length_1 = strlen(word_1);
    int length_2 = strlen(word_2);

    // initial player score
    int player_1_score = 0;
    int player_2_score = 0;

    for (int i = 0; i < length_1; i++)
    {
        player_1_score += char_checker(word_1[i]);
    }

    for (int j = 0; j < length_2; j++)
    {
        player_2_score += char_checker(word_2[j]);
    }

    if (player_1_score > player_2_score)
    {
        printf("Player 1 wins!\n");
    }
    else if (player_1_score < player_2_score)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int char_checker(char letter)
{
    // check based on 2 point value
    if (letter == 68 || letter == 100 || letter == 71 || letter == 103)
    {
        return 2;
    }
    // check based on 3 point value
    else if (letter == 66 || letter == 98 || letter == 67 || letter == 99 || letter == 77 || letter == 109 || letter == 80 ||
             letter == 112 || letter == 88 || letter == 120)
    {
        return 3;
    }
    // check based on 4 point value
    else if (letter == 70 || letter == 102 || letter == 72 || letter == 104 || letter == 86 || letter == 118 || letter == 87 ||
             letter == 119 || letter == 89 || letter == 121)
    {
        return 4;
    }
    // check based on 5 point value
    else if (letter == 75 || letter == 107)
    {
        return 5;
    }
    // check based on 8 point value
    else if (letter == 74 || letter == 106 || letter == 88 || letter == 120)
    {
        return 8;
    }
    // check based on 10 point value
    else if (letter == 81 || letter == 113 || letter == 90 || letter == 122)
    {
        return 10;
    }
    // check if the letter is not alphabeth
    else if (letter < 65 || letter > 122)
    {
        return 0;
    }
    // check if the letter is a symbol or not
    else if (letter > 90 && letter < 96)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
