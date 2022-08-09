print("""Create a string and print its length using len() function.""")
while True:
    a_string = input("Please Enter a string: ")
    if a_string == 'q':
        break
    print(f'Length of input string: {len(a_string)}')

