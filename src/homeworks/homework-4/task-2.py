def get_binary(number):
    integer = int(abs(number))
    fractional = abs(number) % 1

    integer_binary = []
    while integer != 0:
        integer_binary.append(integer % 2)
        integer //= 2
    integer_binary.reverse()

    fractional_binary = []
    while fractional != int(fractional):
        fractional_binary.append(int(fractional * 2))
        fractional = fractional * 2 % 1

    return integer_binary, fractional_binary


def get_exponential_normalized(bin_integer, bin_fractional, sign):
    if bin_integer:
        order = len(bin_integer)
        return f"{sign}0.{''.join(map(str, bin_integer))}{''.join(map(str, bin_fractional))}*2^{order}"

    order = 0
    for i in bin_fractional:
        if i == 0:
            order -= 1
        else:
            break

    return f"{sign}0.{''.join(map(str, bin_fractional[-order:]))}*2^({order})"


def get_number_in_format(integer, frac, sign, num_format):
    if num_format == 1:
        exponent_bit = 11
        mantissa_bit = 52

    elif num_format == 2:
        exponent_bit = 8
        mantissa_bit = 23

    else:
        exponent_bit = 5
        mantissa_bit = 10

    order = len(integer) - 1
    frac = integer[1:] + frac
    shifted_order = get_binary(order + 2 ** (exponent_bit - 1) - 1)[0]

    if len(frac) <= mantissa_bit:
        while len(frac) != mantissa_bit:
            frac.append(0)
    else:
        frac = frac[:mantissa_bit]

    if sign == "+":
        return f"0 {''.join(map(str, shifted_order))} {''.join(map(str, frac))}"
    return f"1 {''.join(map(str, shifted_order))} {''.join(map(str, frac))}"


def main(number, num_format):
    sign_number = "+"
    if number < 0:
        sign_number = "-"

    integer_bin, frac_bin = get_binary(number)

    print(f"Result: {get_exponential_normalized(integer_bin, frac_bin, sign_number)}")

    if num_format == 1:
        print(
            f"Number in FP64: {get_number_in_format(integer_bin, frac_bin, sign_number, num_format)}"
        )
    elif num_format == 2:
        print(
            f"Number in FP32: {get_number_in_format(integer_bin, frac_bin, sign_number, num_format)}"
        )
    else:
        print(
            f"Number in FP16: {get_number_in_format(integer_bin, frac_bin, sign_number, num_format)}"
        )


def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    input_number = input("Enter a number: ")
    while not is_number(input_number):
        input_number = input("Not a number entered. Try again: ")

    print("Choose a format:\n 1)FP64\n 2)FP32\n 3)FP16")
    number_format = input("Selected format: ")
    while not number_format.isdigit() or number_format not in ["1", "2", "3"]:
        number_format = input("Incorrect input. Try again: ")

    main(float(input_number), int(number_format))
