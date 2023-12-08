from src.practice.practice_9.FSM_module import *

IN_FIRST_DFA = "A string from the language: (a|b)*abb"
IN_SECOND_DFA = "A string from the language: digit+(.digit+)?(E(+|-)?digit+)?"
NOT_IN_FSM = "The language of the entered string was not found"


def create_first_dfa() -> FSMachine:
    alphabet = ["a", "b"]
    start_state = 0
    end_states = [3]
    transitions = {
        0: {"b": 0, "a": 1},
        1: {"a": 1, "b": 2},
        2: {"a": 1, "b": 3},
        3: {"a": 1, "b": 0},
    }

    return create_fs_machine(alphabet, transitions, start_state, end_states)


def create_dict_with_digit(now_dict: dict, end_state: int) -> dict:
    new_dict = now_dict
    for i in range(10):
        new_dict[str(i)] = end_state

    return new_dict


def create_second_dfa() -> FSMachine:
    alphabet = [".", "E", "+", "-"]
    for num in range(10):
        alphabet.append(str(num))

    start_state = 0
    end_states = [1]

    transitions = {
        0: create_dict_with_digit(dict(), 1),
        1: {".": 2, "E": 3},
        2: create_dict_with_digit(dict(), 1),
        3: {"+": 4, "-": 4},
        4: create_dict_with_digit(dict(), 1),
    }
    transitions[1] = create_dict_with_digit(transitions[1], 1)
    transitions[3] = create_dict_with_digit(transitions[3], 1)

    return create_fs_machine(alphabet, transitions, start_state, end_states)


def main():
    first_dfa = create_first_dfa()
    second_dfa = create_second_dfa()

    string = input("To check, enter the following line: ")
    if validate_string(first_dfa, string):
        print(IN_FIRST_DFA)

    elif validate_string(second_dfa, string):
        print(IN_SECOND_DFA)

    else:
        print(NOT_IN_FSM)


if __name__ == "__main__":
    main()
