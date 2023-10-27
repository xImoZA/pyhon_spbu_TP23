from sys import argv
import os.path
import string


def get_number_letters_str(str_from_file):
    global number_repetitions

    for letter in string.ascii_lowercase:
        if str_from_file.count(letter) != 0:
            number_repetitions[letter] = number_repetitions.get(
                letter, 0
            ) + str_from_file.count(letter)

    for letter in string.ascii_uppercase:
        if str_from_file.count(letter) != 0:
            number_repetitions[letter] = number_repetitions.get(
                letter, 0
            ) + str_from_file.count(letter)


def read_input_file(file):
    with open(file, "r") as open_file:
        for line in open_file.readlines():
            get_number_letters_str(line)


def write_in_file(file, dict_counts):
    with open(file, "w") as writing_file:
        sorted_letter = sorted(dict_counts.items(), key=lambda x: x[0])
        for letter in sorted_letter:
            writing_file.write(f"{letter[0]}: {letter[1]} \n")


if __name__ == "__main__":
    f, g = argv[1:]

    if not os.path.exists(f):
        print(f"File {f} not exist")

    elif os.path.exists(g):
        print(f"File {g} already exist")

    else:
        number_repetitions = {}
        read_input_file(f)
        write_in_file(g, number_repetitions)
