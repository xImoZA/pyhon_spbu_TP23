from collections import namedtuple
from dataclasses import dataclass

StackElement = namedtuple("StackElement", ["value", "next"])


@dataclass
class Stack:
    size: int
    head: StackElement


def create_new_stack():
    stack = Stack(0, None)
    return stack


def empty(stack):
    return stack.size == 0


def size(stack):
    if not empty(stack):
        return stack.size


def top(stack):
    if not empty(stack):
        return stack.head.value
    return None


def push(stack, value):
    stack.size += 1
    stack.head = StackElement(value, stack.head)


def pop(stack):
    if not empty(stack):
        stack.head = stack.head.next
        stack.size -= 1
        return True
    return None


def main():
    test_stack = create_new_stack()
    pop(test_stack)
    for i in range(10):
        push(test_stack, i)
    print(f"Size stack: {size(test_stack)}")
    print(f"Top element: {top(test_stack)}")
    pop(test_stack)
    print(f"New top element: {top(test_stack)}")
    print(f"New size stack: {size(test_stack)}")


if __name__ == "__main__":
    main()
