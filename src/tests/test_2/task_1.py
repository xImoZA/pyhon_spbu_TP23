INPUT = "Enter the number of the Fibonacci number: "
ERROR_NOT_NUMBER = "Not a number entered"
INVALID_NUMBER = "n can only be from 0 to 90"


def get_fibonacci(num: int) -> int:
    if num == 0:
        return 0

    before_last_num = 0
    last_num = 1

    for i in range(num - 1):
        before_last_num, last_num = last_num, before_last_num + last_num

    return last_num


def is_num(string: str) -> bool:
    try:
        float(string)
        return True

    except ValueError:
        return False


def main() -> None:
    n = input(INPUT)
    if not is_num(n):
        print(ERROR_NOT_NUMBER)
        return

    if int(n) < 0 or int(n) > 90:
        print(INVALID_NUMBER)
        return

    print(f"The {n} fibonacci number: {get_fibonacci(int(n))}")


if __name__ == "__main__":
    main()
