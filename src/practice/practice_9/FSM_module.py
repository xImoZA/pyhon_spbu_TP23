from dataclasses import dataclass


@dataclass
class FSMachine:
    states: dict[int, dict[str, int]]
    start_state: int
    terminal_states: list[int]


def create_fs_machine(
    transitions: dict[int, dict[str, int]],
    start: int,
    end_states: list[int],
) -> FSMachine:
    return FSMachine(transitions, start, end_states)


def validate_string(fsm: FSMachine, string: str) -> bool:
    now_state = fsm.start_state
    for element in string:
        transitions = fsm.states[now_state]
        now_state = ""

        for keys in transitions.keys():
            if element in keys:
                now_state = transitions[keys]
                break

        if now_state == "":
            return False

    return now_state in fsm.terminal_states
