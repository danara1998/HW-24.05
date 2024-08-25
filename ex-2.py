# Создайте вложенный список размером 3*3 через функцию. И посчитайте сумму
# элементов главной диагонали.

matrix = []

def make_matrix():
    inner_list_1 = []
    for i in range(3):
        value = int(input('Введите любое число: '))
        inner_list_1.append(value)
    matrix.append(inner_list_1)
    inner_list_2 = []
    for i in range(3):
        value = int(input('Введите любое число: '))
        inner_list_2.append(value)
    matrix.append(inner_list_2)
    inner_list_3 = []
    for i in range(3):
        value = int(input('Введите любое число: '))
        inner_list_3.append(value)
    matrix.append(inner_list_3)
    print(matrix)
    main_diagonal = matrix[0][0] + matrix[1][1] + matrix[2][2]
    print(main_diagonal)
    
make_matrix()