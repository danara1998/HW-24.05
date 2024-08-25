# Напишите функцию, которая проверяет является ли число степенью двойки. Если 
# истинно выведите True, иначе False.

def degree_of_2():
    number = int(input('Введите число: '))
    while number % 2 == 0:
        number = number / 2 
    if number == 1:
        print(True)
    else:
        print(False)

degree_of_2()