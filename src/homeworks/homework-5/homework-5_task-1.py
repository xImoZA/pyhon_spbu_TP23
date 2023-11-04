def get_binary(number):
    if number < 0:
        number_binary = [1]
    else:
        number_binary = [0]
    variable_number = abs(number)

    while variable_number != 0:
        number_binary.insert(1, variable_number % 2)
        variable_number //= 2

    if number < 0:
        number_binary = addition_binary(get_reverse_code(number_binary), get_binary(1))

    return number_binary


def get_reverse_code(number):
    reverse_number = [1]

    for i in range(1, len(number)):
        reverse_number.append(1 - number[i])

    return reverse_number


def get_same_bit_depth(num_1, num_2):
    if len(num_1) != len(num_2):
        max_num = max(num_1, num_2, key=len)[:]
        min_num = min(num_1, num_2, key=len)[:]

        min_num = [min_num[0]] * (len(max_num) - len(min_num) + 1) + min_num[1:]

        return max_num, min_num
    return num_1, num_2


def addition_binary(number_1, number_2):
    num_1, num_2 = get_same_bit_depth(number_1, number_2)

    num_1.reverse()
    num_2.reverse()

    bin_sum = [0] * len(num_1)

    for i in range(len(bin_sum)):
        bin_sum[i] += num_1[i] + num_2[i]

        if bin_sum[i] > 1:
            if i != len(num_1) - 1:
                bin_sum[i + 1] += 1

            bin_sum[i] = bin_sum[i] % 2

    if num_1[-1] == num_2[-1] and num_1[-1] != bin_sum[-1]:
        bin_sum.append(num_1[-1])

    return list(reversed(bin_sum))


def get_decimal(number):
    decimal_number = 0
    if number[0] == 1:
        number = get_reverse_code(addition_binary(number, get_binary(-1)))

    number = number[::-1]
    for i in range(len(number[:-1])):
        decimal_number += number[i] * (2**i)

    if number[-1] == 1:
        return -decimal_number

    return decimal_number


if __name__ == "__main__":
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    bin_first = get_binary(first_number)
    bin_second = get_binary(second_number)
    sum_numbers = addition_binary(bin_first, bin_second)
    difference_numbers = addition_binary(bin_first, get_binary(-second_number))

    print(
        f'The first number in decimal: {first_number}, in binary: {"".join(map(str, bin_first))}'
    )
    print(
        f'The second number in decimal: {second_number}, in binary: {"".join(map(str, bin_second))}'
    )
    print(
        f'Their sum in binary: {"".join(map(str, sum_numbers))}, in decimal: {get_decimal(sum_numbers)}'
    )
    print(
        f'Their difference in binary: {"".join(map(str, difference_numbers))}, in decimal: {get_decimal(difference_numbers)}'
    )
