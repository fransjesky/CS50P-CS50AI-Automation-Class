"""
In The Sound of Music, there's a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn't grammatically correct, since it would typically be written (with an Oxford comma) as:

Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn't even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 
 names with 
 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""

def main():
    names: list[str] = []
    while True:
        try:
            name: str = input("Name: ")
            names.append(name)
        except EOFError:
            break

    if len(names) == 1:
        print("Adieu, adieu, to", names[0])
    elif len(names) == 2:
        print("Adieu, adieu, to", names[0] + " and " + names[1])
    else:
        name_list: str = ""
        for index in range(len(names)):
            if index != len(names) - 1:
                name_list += names[index] + ", "
            else:
                name_list += "and " + names[index]
        print("Adieu, adieu, to", name_list)


main()
