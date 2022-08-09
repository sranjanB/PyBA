print(
"""

Create two strings, concatenate them, and print the resulting
string.

"""
)
def conc():
    while True:
        a_string = input("Enter string1: ")
        if a_string == 'q':
            break
        b_string = input("Enter string2: ")
        print("concatinating them now.")
        print(a_string +" "+b_string)
