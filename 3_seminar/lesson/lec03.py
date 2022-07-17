# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. сохраните список в формате JSON.
import json

list = []

N = int(input('Введите значение N: '))

def spisok(n):
    for i in range(- n, n + 1):
        list.append(i)
    print(list)
        
spisok(N)

with open('data.json', 'a', encoding='utf-8') as fh:  # открываем файл на чтение
                fh.write(json.dumps(list, ensure_ascii=False))    # загружаем из файла данные в словарь data
print('Данные в формате Json успешно сохранены')

with open('file.txt', 'w') as fh:
                fh.write(str(list))    
print('Данные в формате Txt успешно сохранены')
fh.close()
