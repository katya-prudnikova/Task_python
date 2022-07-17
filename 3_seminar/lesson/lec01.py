# Задайте список из n чисел ряда фибоначчи

list = []
n = int(input('Введите значение n: '))

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)      

for e in range(1, n):
    list.append(fib(e))

print(list)       