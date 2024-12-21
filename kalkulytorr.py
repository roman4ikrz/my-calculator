x = int(input("сколько цифр у вас будет? "))
a = input("введите знак:  ")
b = int(input("введите число 1: "))
c = int(input("введите число 2: "))
g = int(input("введите число 3: ")) if x > 2 else 0

# алгоритм с +
if a == "+":
    if x == 2:
        print("результат: ", b + c)
    elif x == 3:
            print("результат: ", b + c + g)

# алгоритм с -
elif a == "-":
    if x == 2:
        print("результат: ", b - c)
    elif x == 3:
            print("результат: ", b - c - g)
# алгоритм с /
elif a == "/":
    if x == 2:
        print("результат: ", b / c)
    elif x == 3:
            print("результат: ", b / c / g)
# алгоритм с *
elif a == "*":
    if x == 2:
        print("результат: ", b * c)
    elif x == 3:
            print("результат: ", b * c * g)
# алгоритм с ^
elif a == "**":
    if x == 2:
        print("результат: ", b ** c)
    elif x == 3:
            print("результат: ", b ** c ** g) pyinstaller -F kalkulytorr.py
