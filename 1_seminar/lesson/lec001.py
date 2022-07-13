# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
''' *Примеры:*
- 5, 25 -> да
- 4, 16 -> да
- 25, 5 -> да
- 8,9 -> нет '''

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

'''def kvadrat(c, d):
    if c == d**2:
        print('да')
    elif d == c**2:
        print('да')
    else:
        print('нет')       
kvadrat(a, b)'''  

'''def SquareNumber(c, d):
    if c == d**2:
        return 'да'
    elif d == c**2:
        return 'да'
    else:
        return 'нет'
print(SquareNumber(a, b))''' 

def SquareNumber(c, d):
    if (c == d**2) or (d == c**2):
        return 'да'
    else:
        return 'нет'
print(SquareNumber(a, b))