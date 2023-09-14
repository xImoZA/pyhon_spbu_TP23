def list_permutation(x, m, n):
    x.reverse()
    x[:n] = x[n - 1::-1]
    x[n:n + m] = x[m + n:n - 1:-1]
    return x


if __name__ == '__main__':
    list_input = list(map(int, input('Для перестановки начала и конца списка введите список через пробел: ').split()))
    m = int(input('Введите m: '))
    n = int(input('Введите n: '))
    print(f'Полученный список:{" ".join(map(str, list_permutation(list_input, m, n)))}')