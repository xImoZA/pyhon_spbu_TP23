def main():
    input_coefficients = input("Enter the coefficients of the equation: ").split()
    while not get_corrected_input(input_coefficients):
        input_coefficients = input("Incorrect input. Try again: ")
    coefficients = list(map(float, input_coefficients))

    print(
        f"Solution of the equation: {' '.join(map(str, solution_equation(coefficients[0], coefficients[1], coefficients[2])))}"
    )


def get_corrected_input(user_input):
    if len(user_input) != 3 and not is_float_numbers(user_input):
        return False
    return True


def is_float_numbers(numbers):
    for number in numbers:
        try:
            float(number)
        except ValueError:
            return False

    return True


def solution_equation(a, b, c):
    if a == b == c == 0:
        return ["X can be anything"]

    elif a == b == 0:
        raise ValueError("The equation has no solutions")

    elif a == 0:
        return solving_linear_equation(b, c)

    else:
        return solution_quadratic_equation(a, b, c)


def solution_quadratic_equation(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        raise ValueError("The discriminant is less than zero")

    elif discriminant == 0:
        return -b / (2 * a)

    res = [(-b + discriminant**0.5) / (2 * a), (-b - discriminant**0.5) / (2 * a)]
    res.sort()

    return res


def solving_linear_equation(b, c):
    return -c / b


if __name__ == "__main__":
    main()
