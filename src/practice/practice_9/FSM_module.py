from dataclasses import dataclass


@dataclass
class FSMachine:
    alphabet: list[str]
    states: dict[int : dict[str:int]]
    s0: int
    F: list[int]


def create_fs_machine(
    alphabet: list[str],
    transitions: dict[int : dict[str:int]],
    start: int,
    end_states: list[int],
) -> FSMachine:
    return FSMachine(alphabet, transitions, start, end_states)


def validate_string(fsm: FSMachine, string: str) -> bool:
    now_state = fsm.s0
    for element in string:
        if element in fsm.alphabet:
            transitions = fsm.states[now_state]

            if element in transitions.keys():
                now_state = transitions[element]

            else:
                return False
        else:
            return False

    return now_state in fsm.F
