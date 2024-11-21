'''
When texting or tweeting, it's not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
'''

temp: str = ""

def main():
    get_input: str = input("Input: ")

    for i in get_input:
        check_char(i)

    print(f"Output:", temp)


def check_char(c: str):
    global temp

    if c not in ("a", "i", "u", "e", "o", "A", "I", "U", "E", "O"):
        temp += c
    else:
        return


main()
