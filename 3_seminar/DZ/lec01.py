# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

list = ['a, 2, 4', 
        't, 6, 2',
        'f, 1, 3']

n = input('Введите некое число: ')

def print_number(n):
    for i in list:
        print(i)
        for a in i:
            if a == str(n):
                print(f'В данной строке списка {i} присутствует некое число {n}')        
                            
print_number(n)    