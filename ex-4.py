# Написать рекурсивную функцию, которая по заданному целому числу возвращает n-e число Фибоначчи
def fib(fibonacci_number):
    if fibonacci_number <= 1:
        return 0
    elif fibonacci_number == 2:
        return 1
    else:
        return fib(fibonacci_number - 1) + fib(fibonacci_number - 2)

fibonacci_number = int(input('Введите номер числа из ряда Фибоначчи: '))
print(fib(fibonacci_number))
5  