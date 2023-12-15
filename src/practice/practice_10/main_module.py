from src.practice.practice_10.parser_module import *


def main():
    string = input("Enter the line: ")
    try:
        parse_tree = parse(string.split())
        pretty_print(parse_tree)
    except TypeError:
        print("The string does not match the grammar")


if __name__ == "__main__":
    main()
