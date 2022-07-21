# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
'''Пример:
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1'''

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
simbol = "qwe"

def replay_simbol(simbol):
    sum = 0
    for i in range(len(list)):
        if simbol == list[i]:
            sum += 1
            if sum == 2:
                print(i)
                break
    if sum < 2:
        print('-1')    
      
replay_simbol(simbol)

'''list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
simbol = "йцу"

def replay_simbol(simbol):
    sum = 0
    for i in range(len(list)):
        if simbol == list[i]:
            sum += 1
            if sum == 2:
                print(i)
                break
    if sum < 2:
        print('-1')    
      
replay_simbol(simbol)'''

'''list = []
simbol = "123"

def replay_simbol(simbol):
    sum = 0
    for i in range(len(list)):
        if simbol == list[i]:
            sum += 1
            if sum == 2:
                print(i)
                break
    if sum < 2:
        print('-1')    
      
replay_simbol(simbol)'''

'''list = ["123", "234", 123, "567"]
simbol = "123"

def replay_simbol(simbol):
    sum = 0
    for i in range(len(list)):
        if simbol == list[i]:
            sum += 1
            if sum == 2:
                print(i)
                break
    if sum < 2:
        print('-1')    
      
replay_simbol(simbol)'''