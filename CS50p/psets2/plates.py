'''
In Massachusetts, home to Harvard University, it's possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a '0'.”
- “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user's input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You're welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
'''

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
marks = [" ", ".", ",", "!", "?"]


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # convert the input to uppercase
    fs: str = s.upper()

    # Check if the input length are between 2 and 6
    if len(fs) < 2:
        return False
    elif len(fs) > 6:
        return False

    # Check if the first 2 characters are letter
    if len(fs) > 1:
        for i in range(2):
            if fs[i] in numbers:
                return False

    # Check if there is a number in the middle
    number_count: int = 0
    for char in fs:
        if char in marks:
            return False
        elif char in numbers and number_count == 0:
            if char == "0":
                return False
            else:
                number_count += 1
        elif char in numbers and number_count > 0:
            number_count += 1
        elif number_count > 0 and char not in numbers:
            return False

    # else return True
    return True


main()
