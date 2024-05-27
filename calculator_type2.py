# Define a function named calculate()
def calculate():
    # Ask the user to input an operator
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    # Ask the user to input two numbers
    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    # Perform the operation based on the user's input
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Ask the user if they want to calculate again
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # If the user types Y, run the calculate() function again
    if calc_again.upper() == 'Y':
        calculate()

    # If the user types N, print a goodbye message and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    else:
        again()

# Call calculate() outside of the function
calculate()