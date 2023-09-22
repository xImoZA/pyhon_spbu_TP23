import random


def create_number():
    number = str(random.randint(1, 9))

    while len(number) != 4:
        digit = random.randint(0, 9)
        if str(digit) not in number:
            number += str(digit)

    return number


def count_bulls_and_cows(input_, answer):
    number_bulls = 0
    for i in range(4):
        if input_[i] == answer[i]:
            number_bulls += 1

    number_cows = 0
    for i in range(4):
        if input_[i] in answer:
            number_cows += 1

    return number_cows - number_bulls, number_bulls


if __name__ == '__main__':
    print('Bulls and cows\n It is necessary to guess a four-digit digit number consisting of non-repeating digits\n'
          'After each move, the computer outputs the number of cows(the number of guessed digits in the wrong '
          'positions) and the number of bulls(the number of guessed digits in their correct positions)')

    answer_number = create_number()

    attempts = 0
    while True:
        attempts += 1
        input_number = input(f'{attempts} attempt. To enter a number: ')

        if input_number != answer_number:
            cows, bulls = count_bulls_and_cows(input_number, answer_number)
            print(f'Found {cows} cows and {bulls} bulls. Try again')
        
        else:
            print(f'You won in {attempts} moves')
            break