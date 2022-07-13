# Изучить понятие Предикатов.

# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

def func(a, b, c):
    if not(a and b and c) == (not a or not b or not c):
        print(True)
    else:
        print(False)

X = float(input('Введите значение X: '))
Y = float(input('Введите значение Y: '))
Z = float(input('Введите значение Z: '))

func(X, Y, Z)    