'''
Question 4
Create a fully commented program to:
allow a user to select a member of the Monty Python team and view details of their date of
birth, place of birth and middle name(s) in any.
'''


print('Choose which member of the group you would like to know about:')
print('Terry Jones')
print('John Cleese')
print('Terry Gilliam')
print('Graham Chapman')
print('Eric Idle')
print('Michael Palin')
menu_choice = input(">> ")

if menu_choice == 'Terry Jones' or menu_choice == 'terry jones':
    print('Date of the birth: 1 February 1942')
    print('Place of birth: Colwyn Bay')
    print('The  middle name(s): Graham Parry')
elif menu_choice == 'John Cleese' or menu_choice == 'john cleese':
    print('Date of the birth: 27 October 1939')
    print('Place of birth: Weston-super-Mare')
    print('The  middle name(s): Marwood')
elif menu_choice == 'Terry Gilliam' or menu_choice == 'terry gilliam':
    print('Date of the birth: 22 November 1940')
    print('Place of birth: Minneapolis')
    print('The  middle name(s): Vance')
elif menu_choice == 'Graham Chapman' or menu_choice == 'graham chapman':
    print('Date of the birth: 8 January 1941')
    print('Place of birth: Stoneygate, Leicester')
    print('The  middle name(s): Arthur')
elif menu_choice == 'Eric Idle' or menu_choice == 'eric idle':
    print('Date of the birth: 29 March 1943')
    print('Place of birth: South Shields')
    print('The  middle name(s): -')
elif menu_choice == 'Michael Palin' or menu_choice == 'michael palin':
    print('Date of the birth: 5 May 1943')
    print('Place of birth: Ranmoor, Sheffield')
    print('The  middle name(s): Edward')
else:
    print('Oops...')