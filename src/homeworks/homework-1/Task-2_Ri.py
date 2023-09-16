from math import acos, pi


def input_vector():
    coordinates = [int(input(f'Введите координату {xyz}{index_xyz}: ')) for xyz in ['x', 'y', 'z']
                   for index_xyz in range(1, 3)]

    return [abs(coordinates[1] - coordinates[0]), abs(coordinates[3] - coordinates[2]),
            abs(coordinates[5] - coordinates[4])]


def input_matrix(str_matrx, column_matrx, numbr):
    print(f'Введите данные {numbr}матрицы')

    matrix = []
    for lines in range(1, str_matrx + 1):
        input_str = list(map(int, input(f'Введите {lines} строку матрицы через пробел: ').split()))

        while len(input_str) != column_matrx:
            input_str = list(map(int, input(f'Введено некорректное число элементов. Попробуйте снова. '
                                            f'\nВведите {lines} строку матрицы через пробел: ').split()))

        matrix += [input_str]

    return matrix


def incorrect_input(output_phrase, correct_input):
    input_number = input(output_phrase)

    while input_number not in correct_input:
        input_number = input('Некорректный ввод, попробуйте снова: ')

    return input_number


def vector_length(vector_value):
    if vector_value[2] == 0:
        return (vector_value[0] ** 2 + vector_value[1] ** 2) ** 0.5

    if vector_value[1] == 0:
        return (vector_value[0] ** 2 + vector_value[2] ** 2) ** 0.5

    if vector_value[0] == 0:
        return (vector_value[1] ** 2 + vector_value[2] ** 2) ** 0.5

    else:
        return (vector_value[0] ** 2 + vector_value[1] ** 2 + vector_value[2] ** 2) ** 0.5


def cos_angle_between_vectors(vector_value_1, vector_value_2):
    numerator = (vector_value_1[0] * vector_value_2[0]) + (vector_value_1[1] * vector_value_2[1]) + \
                  (vector_value_1[2] * vector_value_2[2])
    denominator_1 = (vector_value_1[0] ** 2 + vector_value_1[1] ** 2 + vector_value_1[2] ** 2) ** 0.5
    denominator_2 = (vector_value_2[0] ** 2 + vector_value_2[1] ** 2 + vector_value_2[2] ** 2) ** 0.5

    return numerator / (denominator_1 * denominator_2)  # если в одну строчку, получается огромная нечитаемая строка(


def scalar_product_vectors(vector_value_1, vector_value_2):
    return vector_length(vector_value_1) * vector_length(vector_value_2) * cos_angle_between_vectors(vector_value_1,
                                                                                                     vector_value_2)


def transposition_matrix(matrix):
    new_matrix = [[matrix[score_str][score_column] for score_str in range(len(matrix))]
                  for score_column in range(len(matrix[0]))]

    return new_matrix


def sum_of_matrices(matrix1, matrix2):
    new_matrix = [[matrix1[score_str][score_column] + matrix2[score_str][score_column]
                   for score_column in range(len(matrix1[0]))] for score_str in range(len(matrix1))]

    return new_matrix


def product_of_matrices(matrix1, matrix2):
    output_matrix = [[sum([matrix1[x][i] * matrix2[i][y] for i in range(len(matrix1[0]))])
                      for y in range(len(matrix2[0]))] for x in range(len(matrix1))]

    return output_matrix


def product_of_matrix_and_number(matrix, num):
    output_matrix = [[matrix[srt_matrx][column_mtrx] * num for column_mtrx in range(len(matrix[srt_matrx]))]
                     for srt_matrx in range(len(matrix))]
    return output_matrix


if __name__ == '__main__':
    type_v_m = incorrect_input('Для того чтобы работать с векторами введите V, чтобы работать с матрицами введите M: ',
                               ['V', 'M'])

    if type_v_m == 'V':
        operation = incorrect_input('Выберите операцию:\n 1)нахождение скалярного произведения \n '
                                    '2)вычисление длины вектора \n 3)нахождение угла между векторами \n '
                                    'Выбранная операция (1/2/3): ', ['1', '2', '3'])

        if operation == '2':
            print('Для выполнения операции, введите координаты вектора')
            vector = input_vector()
            print(f'Вычисленная длина вектора: {vector_length(vector)}')

        else:
            print('Для выполнения операции, введите координаты первого вектора')
            vector_1 = input_vector()

            print('Введите координаты второго вектора')
            vector_2 = input_vector()

            if operation == '1':
                print(f'Вычисленное произведение: {scalar_product_vectors(vector_1, vector_2)}')

            elif operation == '3':
                print(f'Вычисленный угол: {acos(cos_angle_between_vectors(vector_1, vector_2)) * 180 / pi}')

    elif type_v_m == 'M':
        operation = incorrect_input('Выберите операцию:\n 1)транспонирование матрицы \n 2)сложение матриц \n '
                                    '3)произведение матриц \n 4)произведение матрицы и числа \n '
                                    'Выбранная операция (1/2/3/4): ', ['1', '2', '3', '4'])
    
        if operation in ['1', '2', '4']:
            str_marix = int(input('Для работы с матрицей введите количество строк матрицы: '))
            columns_matrix = int(input('Введите количество столбцов: '))

            if operation == '1':
                print('Транспонированная матрица:')
                print('\n'.join(' '.join(map(str, i)) for i in transposition_matrix(input_matrix(str_marix,
                                                                                                 columns_matrix, ''))))
            elif operation == '2':
                input_matrix_1 = input_matrix(str_marix, columns_matrix, 'первой ')
                input_matrix_2 = input_matrix(str_marix, columns_matrix, 'второй ')

                print('Сумма матриц:')
                print('\n'.join(' '.join(map(str, i)) for i in sum_of_matrices(input_matrix_1, input_matrix_2)))

            elif operation == '4':
                input_matrix = input_matrix(str_marix, columns_matrix, '')
                number = int(input('Введите число, на которое нужно умножить матрицу: '))

                print('Полученная матрица:')
                print('\n'.join(' '.join(map(str, i)) for i in product_of_matrix_and_number(input_matrix, number)))

        elif operation == '3':
            str_marix_1 = int(input('Для работы с матрицей введите количество строк первой матрицы: '))
            columns_matrix_1 = int(input('Введите количество столбцов первой матрицы: '))
            input_matrix_1 = input_matrix(str_marix_1, columns_matrix_1, 'первой ')

            str_marix_2 = columns_matrix_1
            columns_matrix_2 = int(input('Введите количество столбцов второй матрицы: '))
            input_matrix_2 = input_matrix(str_marix_2, columns_matrix_2, 'второй ')

            print('Произведение матриц:')
            print('\n'.join(' '.join(map(str, i)) for i in product_of_matrices(input_matrix_1, input_matrix_2)))
