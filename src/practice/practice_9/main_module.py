import string

from src.practice.practice_9.FSM_module import *

IN_DFA = "A string from the language: "
NOT_IN_FSM = "The language of the entered string was not found"
LANGUAGE = ["(a|b)*abb", "digit+(.digit+)?(E(+|-)?digit+)?"]


def create_dfa(name_language: str) -> FSMachine:
    if name_language == LANGUAGE[0]:
        start_state = 0
        end_states = [3]
        transitions = {
            0: {"b": 0, "a": 1},
            1: {"a": 1, "b": 2},
            2: {"a": 1, "b": 3},
            3: {"a": 1, "b": 0},
        }

    elif name_language == LANGUAGE[1]:
        start_state = 0
        end_states = [1, 3, 6]
        transitions = {
            0: {string.digits: 1},
            1: {".": 2, "E": 4, string.digits: 1},
            2: {string.digits: 3},
            3: {"E": 4, string.digits: 3},
            4: {"+": 5, "-": 5, string.digits: 6},
            5: {string.digits: 6},
            6: {string.digits: 6},
        }

    return create_fs_machine(transitions, start_state, end_states)


def main() -> None:
    dfa_machines = []
    for language in LANGUAGE:
        dfa_machines.append(create_dfa(language))

    input_str = input("To check, enter the following line: ")
    for i in range(len(dfa_machines)):
        if validate_string(dfa_machines[i], input_str):
            print(IN_DFA + LANGUAGE[i])
            return

    print(NOT_IN_FSM)


if __name__ == "__main__":
    main()
