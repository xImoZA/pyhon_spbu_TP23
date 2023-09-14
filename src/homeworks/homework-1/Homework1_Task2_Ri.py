from math import acos, pi


def input_vector():
    return list(map(int, input('Введите вектор: ').split()))


def get_input_matrix(str_matrx, column_matrx):
    print(f'Введите данные матрицы')

    input_matrix = []
    for lines in range(1, str_matrx + 1):
        input_str = list(map(int, input(f'Введите {lines} строку матрицы через пробел: ').split()))

        while len(input_str) != column_matrx:
            input_str = list(map(int, input(f'Введено некорректное число элементов. Попробуйте снова. '
                                            f'\nВведите {lines} строку матрицы через пробел: ').split()))

        input_matrix += [input_str]

    return input_matrix


def get_correct_input(output_phrase, correct_input):
    input_number = input(output_phrase)

    while input_number not in correct_input:
        input_number = input('Некорректный ввод, попробуйте снова: ')

    return input_number


def vector_length(vector_value):
    return (sum([i ** 2 for i in vector_value])) ** 0.5


def angle_between_vectors(vector_value_1, vector_value_2):
    return acos(scalar_product_vectors(vector_value_1, vector_value_2) /
                (vector_length(vector_value_1) * vector_length(vector_value_2))) * 180 / pi


def scalar_product_vectors(vector_value_1, vector_value_2):
    return sum([vector_value_1[i] * vector_value_2[i] for i in range(len(vector_value_1))])


def transposition_matrix(matrix):
    return [[matrix[score_str][score_column] for score_str in range(len(matrix))]
            for score_column in range(len(matrix[0]))]


def sum_of_matrices(matrix1, matrix2):
    return [[matrix1[score_str][score_column] + matrix2[score_str][score_column]
             for score_column in range(len(matrix1[0]))] for score_str in range(len(matrix1))]


def scalar_product_of_matrices(matrix1, matrix2):
    new_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for x in range(len(matrix1)):
        for y in range(len(matrix2[0])):
            for i in range(len(matrix1[0])):
                new_matrix[x][y] += matrix1[x][i] * matrix2[i][y]

    return new_matrix


def product_of_matrix_and_number(matrix, num):
    for srt_matrx in range(len(matrix)):
        for column_mtrx in range(len(matrix[srt_matrx])):
            matrix[srt_matrx][column_mtrx] *= num

    return matrix


def operation_vectors_13(parameter):
    print('Первый вектор')
    vector_1 = input_vector()

    print('Второй вектор')
    vector_2 = input_vector()

    if parameter == '1':
        return f'Вычисленное произведение: {scalar_product_vectors(vector_1, vector_2)}'
    return f'Вычисленный угол: {angle_between_vectors(vector_1, vector_2)}'


def operation_matrix_124(parameter):
    str_marix = int(input('Для работы с матрицей введите количество строк матрицы: '))
    columns_matrix = int(input('Введите количество столбцов: '))

    if parameter == '1':
        print('Транспонированная матрица:')
        return '\n'.join(' '.join(map(str, i)) for i in transposition_matrix(get_input_matrix(str_marix,
                                                                                              columns_matrix)))
    elif parameter == '2':
        input_matrix_1 = get_input_matrix(str_marix, columns_matrix)
        input_matrix_2 = get_input_matrix(str_marix, columns_matrix)

        print('Сумма матриц:')
        return '\n'.join(' '.join(map(str, i)) for i in sum_of_matrices(input_matrix_1, input_matrix_2))

    elif parameter == '4':
        input_matrix = get_input_matrix(str_marix, columns_matrix)
        number = int(input('Введите число, на которое нужно умножить матрицу: '))

        print('Полученная матрица:')
        return '\n'.join(' '.join(map(str, i)) for i in product_of_matrix_and_number(input_matrix, number))


def operation_matrix_3():
    str_marix_1 = int(input('Для работы с матрицей введите количество строк первой матрицы: '))
    columns_matrix_1 = int(input('Введите количество столбцов первой матрицы: '))
    input_matrix_1 = get_input_matrix(str_marix_1, columns_matrix_1)

    str_marix_2 = columns_matrix_1
    columns_matrix_2 = int(input('Введите количество столбцов второй матрицы: '))
    input_matrix_2 = get_input_matrix(str_marix_2, columns_matrix_2)

    print('Произведение матриц:')
    return '\n'.join(' '.join(map(str, i)) for i in scalar_product_of_matrices(input_matrix_1, input_matrix_2))


if __name__ == '__main__':
    type_v_m = get_correct_input(
        'Для того чтобы работать с векторами введите V, чтобы работать с матрицами введите M: ', ['V', 'M'])

    if type_v_m == 'V':
        operation = get_correct_input('Выберите операцию:\n 1)нахождение скалярного произведения \n '
                                      '2)вычисление длины вектора \n 3)нахождение угла между векторами \n '
                                      'Выбранная операция (1/2/3): ', ['1', '2', '3'])

        if operation == '2':
            vector = input_vector()
            print(f'Вычисленная длина вектора: {vector_length(vector)}')

        elif operation in ['1', '3']:
            print(operation_vectors_13(operation))

    elif type_v_m == 'M':
        operation = get_correct_input('Выберите операцию:\n 1)транспонирование матрицы \n 2)сложение матриц \n '
                                      '3)произведение матриц \n 4)произведение матрицы и числа \n '
                                      'Выбранная операция (1/2/3/4): ', ['1', '2', '3', '4'])

        if operation in ['1', '2', '4']:
            print(operation_matrix_124(operation))

        elif operation == '3':
            print(operation_matrix_3())
