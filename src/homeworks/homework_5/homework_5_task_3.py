from dataclasses import dataclass
from collections import namedtuple

QueueElement = namedtuple("QueueElement", ["value", "next"])


@dataclass
class Queue:
    size: int
    head: QueueElement
    tail: QueueElement


def create_new_queue():
    return Queue(0, None, None)


def empty(queue):
    return queue.size == 0


def size(queue):
    return queue.size


def top(queue):
    if not empty(queue):
        return queue.head.value
    return None


def last(queue):
    if not empty(queue):
        return queue.tail.value
    return None


def push(queue, value):
    element = QueueElement(value, None)

    if empty(queue):
        queue.head = element

    elif queue.size == 1:
        queue.tail = element
        queue.head = QueueElement(queue.head.value, queue.tail)

    else:
        queue.tail = QueueElement(value, element)
        queue.tail = element

    queue.size += 1


def pop(queue):
    if not empty(queue):
        queue.head = queue.head.next
        queue.size -= 1
