from collections import namedtuple
from dataclasses import dataclass

StackElement = namedtuple("StackElement", ["value", "next"])


@dataclass
class Stack:
    size: int
    head: StackElement


def create_new_stack():
    stack = Stack(0, (None, None))
    return stack


def empty(stack):
    return stack.size == 0


def size(stack):
    if empty(stack):
        return stack.size


def top(stack):
    if empty(stack):
        return stack.head.value
    return False


def push(stack, value):
    stack.size += 1
    stack.head = StackElement(value, stack.head)


def pop(stack):
    if empty(stack):
        stack.head = stack.head.next
        stack.size -= 1
        return True
    return False


def main():
    test_stack = create_new_stack()
    pop(test_stack)
    for i in range(10):
        push(test_stack, i)
    print(size(test_stack))
    print(top(test_stack))
    pop(test_stack)
    print(top(test_stack))
    print(size(test_stack))


if __name__ == "__main__":
    main()
