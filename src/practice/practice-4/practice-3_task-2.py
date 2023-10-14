import random


def create_number(input_number_length):
    number = str(random.randint(1, 9))

    while len(number) != input_number_length:
        digit = random.randint(0, 9)
        if str(digit) not in number:
            number += str(digit)

    return number


def count_bulls_and_cows(input_, answer, input_number_length):
    number_bulls = 0
    number_cows = 0
    for i in range(input_number_length):
        if input_[i] == answer[i]:
            number_bulls += 1

        elif input_[i] in answer:
            number_cows += 1

    return number_cows, number_bulls


if __name__ == "__main__":
    rules = (
        "Bulls and cows\nIt is necessary to guess a four-digit digit number consisting of non-repeating digits\n"
        "After each move, the computer outputs the number of cows(the number of guessed digits in the wrong "
        "positions) and the number of bulls(the number of guessed digits in their correct positions)"
    )
    print(rules)

    number_length = input("Input length the intended number: ")
    while not number_length.isdigit():
        number_length = input("Incorrect input. Input length the intended number: ")
    number_length = int(number_length)

    answer_number = create_number(number_length)

    attempts = 0
    while True:
        attempts += 1
        input_number = input(f"{attempts} attempt. To enter a number: ")
        while not input_number.isdigit():
            input_number = input(
                f"Incorrect input. {attempts} attempt. To enter a number: "
            )

        if input_number != answer_number:
            cows, bulls = count_bulls_and_cows(
                input_number, answer_number, number_length
            )
            print(f"Found {cows} cows and {bulls} bulls. Try again")

        else:
            print(f"You won in {attempts} moves")
            break
