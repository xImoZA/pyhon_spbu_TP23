def main():
    input_coefficients = input("Enter the coefficients of the equation: ").split()

    try:
        is_input_correct(input_coefficients)
    except ValueError as error:
        print(f"Error: {error}")

    coefficients = list(map(float, input_coefficients))

    try:
        solve_of_equation = get_beautiful_numbers(
            solve_equation(coefficients[0], coefficients[1], coefficients[2])
        )
        print(f"Solution of the equation: {' '.join(map(str, solve_of_equation))}")
    except ValueError as error:
        print(f"Error: {error}")


def get_beautiful_numbers(answer):
    beautiful_numbers = [
        int(number) if int(number) == number else number for number in answer
    ]

    return tuple(beautiful_numbers)


def is_input_correct(user_input):
    if len(user_input) != 3:
        raise ValueError("More than 3 arguments have been entered")

    for i in range(len(user_input)):
        if not is_float_number(user_input[i]):
            raise ValueError(f"Invalid argument №{i + 1}")

    return True


def is_float_number(number):
    try:
        float(number)
        return True

    except ValueError:
        return False


def solve_equation(a, b, c):
    if a == b == c == 0:
        raise ValueError("X can be anything")

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
        return (-b / (2 * a),)

    return (-b + discriminant**0.5) / (2 * a), (-b - discriminant**0.5) / (2 * a)


def solving_linear_equation(b, c):
    return (-c / b,)


if __name__ == "__main__":
    main()
