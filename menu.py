# This program is used as a menu where a person will store numbers inot an array adn have the option to start the progma and enter a numerb to printer what they have enter so far 
# 
y = []


# The function will display the menu options: Start or Exit.
# If the user selects a continuation option, they will be prompted to enter a number.
# If they choose to exit, they can type 'exit' to terminate the script and consequently remove the data.
def menu(): 

    while True:
        x = input('''
1. Start
2. Print  
3. End
''')
        if x == 'end':
            print('goodbye') 
            break
        # will end the program

        elif x == 'print':
            print(y)
            # will display the stored numbers

        elif x == 'start':
            a = input("Please enter a number: ")
            y.append(a)
            # It will start the program and add it to the array.


menu()
