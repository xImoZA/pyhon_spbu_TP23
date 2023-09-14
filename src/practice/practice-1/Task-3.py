def prime_numbers(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def all_prime_numbers(x):
    output = [i for i in range(1, x) if prime_numbers(i)]
    return output


if __name__ == '__main__':
    number_input = int(input('Чтобы узнать все простые числа до некоторого n, введите n: '))
    print(f'Все числа: {" ".join(map(str, all_prime_numbers(number_input)))}')