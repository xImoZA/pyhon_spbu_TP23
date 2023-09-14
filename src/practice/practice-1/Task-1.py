def division(a, b):
    whole_private = 0
    while a >= b:
        a -= b
        whole_private += 1
    return whole_private


if __name__ == '__main__':
    print('Для вычисления частного')
    print('Введите а:')
    divisible = int(input())
    print('Введите b:')
    divider = int(input())
    print(f'Частное от деления:{division(divisible, divider)}')