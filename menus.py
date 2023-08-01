'''Menus'''

print('Please select one of the following:')
print('Type A if you want to ADD')
print('Type S if you want to SUBTRACT')
print('Type M if you want to MULTIPLY')
print('Type D if you want to DIVIDE')
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
else:
    print('Invalid entry')
'''
menu_choice == 'A' or 'a' -------------- DOESN'T WORK
'''