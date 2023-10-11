from sys import argv
import os.path


def sort_file(name_read_file, name_write_file, input_a, input_b):
    less_a = []
    more_a_less_b = []
    more_b = []
    with open(name_read_file, "r") as file:
        for number in list(map(int, file.readline().split())):
            if number < input_a:
                less_a += [str(number)]
            elif input_a <= number <= input_b:
                more_a_less_b += [str(number)]
            else:
                more_b += [str(number)]

    with open(name_write_file, "w") as write_file:
        write_file.write(f'Numbers less than {input_a}: {" ".join(less_a)}\n')
        write_file.write(
            f'Numbers greater than {input_a} and less than {input_b}: {" ".join(more_a_less_b)}\n'
        )
        write_file.write(f'Other numbers: {" ".join(more_b)}')


if __name__ == "__main__":
    a, b, f, g = argv[1:]
    a = int(a)
    b = int(b)

    if not os.path.exists(f):
        print(f"File {f} not exist")
    elif os.path.exists(g):
        print(f"File {g} already exist")
    else:
        sort_file(f, g, a, b)
        print(f"The sorted numbers is written to {g}")
