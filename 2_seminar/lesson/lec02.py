'''В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу, по которой робот, 
когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".

Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова.

Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное), 
выводящее это число в консоль вместе с правильным образом изменённым словом "программист", для того, чтобы робот 
мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.

В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.'''

for i in range(0,50,1):
   abv(i)

def abv(num):
    if (num == 1) or (num > 20 and num % 10 == 1) or (num > 99 and num % 100 == 1):
        print(f'{num} - программист')
    elif (2 <= num <= 4) or (num > 20 and 2 <= num % 10 <= 4) or (num > 99 and 2 <= num % 100 <= 4):
        print(f'{num} - программиста')
    else:
        print(f'{num} - программистов')

