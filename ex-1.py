# Напишите программу для создания списка, длина которого равна N. После создания 
# списка нужно подсчитать нечетные и четные числа. Если нечетных чисел больше, чем четных,
# вывод должен быть «Нет», в остальных ключах «Да». 

def even_nums(n):
    numbers = []
    for i in range(n):
        numbers.append(int(input('Введите число: ')))
    even_numbers = []
    odd_numbers = []
    for x in numbers:
        if x % 2 == 0:
            even_numbers.append(x)
        else:
            odd_numbers.append(x)
    print(odd_numbers)
    print(even_numbers)
    if len(odd_numbers) > len(even_numbers):
        print('No')
    else:
        print('Yes')
            
n = int(input('Введите количество чисел: '))
even_nums(n)