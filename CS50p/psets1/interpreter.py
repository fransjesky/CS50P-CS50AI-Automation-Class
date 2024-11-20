'''
Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables users to do math, even without knowing Python.

In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!
'''

def main():
    user_input: str = input("Expression: ")
    finput: str = user_input.split(' ')
    x: int = int(finput[0])
    y: int = int(finput[2])
    operator: str = finput[1]

    do_math(x, y, operator)

def do_math(x: int, y: int, operator: str):
    match operator:
        case "+":
            print(f"{float(x + y):.1f}")
        case "-":
            print(f"{float(x - y):.1f}")
        case "*":
            print(f"{float(x * y):.1f}")
        case "/":
            print(f"{float(x / y):.1f}")
        case _:
            print("Not a Number")


main()
