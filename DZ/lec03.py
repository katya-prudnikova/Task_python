# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Введите значение координаты точки X = ')
x = float(input())
print('Введите значение координаты точки Y = ')
y = float(input())

def print_quarter(a, b):
    while (a == 0 and b == 0):
        a = input('Вы ввели неправильные значения, попробуйте еще раз: \nВведите X = ')
        b = input('Введите Y = ')
    else:
        a, b = float(a), float(b)
        if a > 0 and y > 0: print('1 четверть')
        elif a < 0 and b > 0: print('2 четверть')
        elif a < 0 and b < 0: print('3 четверть')
        elif a > 0 and b < 0: print('4 четверть')
        elif a == 0: print('Точка находится на оси X')
        elif b == 0: print('Точка находится на оси Y')

print_quarter(x, y)        