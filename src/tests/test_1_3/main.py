from src.tests.test_1_3.merge_sort import *


def main():
    try:
        array = list(
            map(
                int,
                input(
                    "Enter a sequence of numbers to sort through the space: "
                ).split(),
            )
        )
        try:
            print(" ".join(map(str, sort(array))))

        except ValueError as e:
            print(e)

    except ValueError:
        print("Non-integers were entered")


if __name__ == "__main__":
    main()
