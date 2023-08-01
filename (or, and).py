'''AND'''

num1 = int(input("num1? >"))
num2 = int(input("num2? >"))
num3 = int(input("num3? >"))
num4 = int(input("num4? >"))
print()
print('Condition 1: ', num1, '<', num2, 'is', (num1 < num2))
print('Condition 2: ', num3, '<', num4, 'is', (num3 < num4))

if (num1 < num2) and (num3 < num4):
    print("Both condition are TRUE")
else:
    print("At least one of the conditions is FALSE")

'''OR'''

num1 = int(input("num1? >"))
num2 = int(input("num2? >"))
num3 = int(input("num3? >"))
num4 = int(input("num4? >"))
print()
print('Condition 1: ', num1, '<', num2, 'is', (num1 < num2))
print('Condition 2: ', num3, '<', num4, 'is', (num3 < num4))

if (num1 < num2) or (num3 < num4):
    print("At least one of the conditions is TRUE")
else:
    print("Both condition are FALSE")