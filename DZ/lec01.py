# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Введите день недели: '))

def week(N):
    if N == 6 or N == 7:
        print('Выходной')
    elif (N > 7 or N < 1):
        print('Введите число от 1 до 7')   
    else:
        print('Будний')  
        
week(day)    