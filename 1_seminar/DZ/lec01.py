# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Введите цифру, обозначающую день недели: '))

def number_week(N):
    if N == 6 or N == 7:
        print('Да')
    elif (N > 7 or N < 1):
        print('Это вообще не день недели')   
    else:
        print('Нет')  

number_week(day)    