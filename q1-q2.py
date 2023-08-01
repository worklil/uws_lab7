'''
Question 1
Create a fully commented version of the A/S/M/D from the lecture.
'''

print('Please select one of the following:')
print('Type A if you want to ADD')
print('Type S if you want to SUBTRACT')
print('Type M if you want to MULTIPLY')
print('Type D if you want to DIVIDE')
print('Type N if you want to know if the number is EVEN or ODD')
print('Type F if you want to FLOOR DIVISION')
print('Type E if you want to EXPONENTIATION')
menu_choice = input(">> ")

num1 = int(input('Enter the first number >>'))
num2 = int(input('Enter the second number >>'))
if menu_choice == 'A' or menu_choice == 'a':
    answer = num1 + num2
    print('If you ADD', num1, 'to', num2, 'you get', answer)
elif menu_choice == 'S' or menu_choice == 's':
    answer = num2 - num1
    print('If you SUBTRACT', num2, 'from', num1, 'you get', answer)
elif menu_choice == 'M' or menu_choice == 'm':
    answer = num1 * num2
    print('If you MULTIPLY', num1, 'by', num2, 'you get', answer)
elif menu_choice == 'D' or menu_choice == 'd':
    if num2 == 0:
        print("Sorry you can't divide by zero")
    else:
        answer = num1/num2
        print('If you DIVIDE', num1, 'by', num2, 'you get', answer)
elif menu_choice == 'N' or menu_choice == 'n':
    answer1 = num1 % 2
    answer2 = num2 % 2
    if answer1 == 0 and answer2 == 0:
        print("They are both EVEN")
    elif answer1 == 1 and answer2 == 1:
        print("They are both ODD")
    else:
        if answer1 == 0:
            print(num1, 'is EVEN')
        elif answer1 == 1:
            print(num1, 'is ODD')
        if answer2 == 0:
            print(num2, 'is EVEN')
        elif answer2 == 1:
            print(num2, 'is ODD')
elif menu_choice == 'F' or menu_choice == 'f':
    if num2 == 0:
        print("Sorry you can't divide by zero")
    else:
        answer = num1//num2
        print('If you FLOOR DIVISION', num1, 'by', num2, 'you get', answer)
elif menu_choice == 'E' or menu_choice == 'e':
    answer = num1 ** num2
    print('If you EXPONENTIATION', num1, 'by', num2, 'you get', answer)

else:
    print('Invalid entry')