from dataclasses import dataclass
from collections import namedtuple

QueueElement = namedtuple("QueueElement", ["value", "next"])


@dataclass
class Queue:
    size: int
    head: QueueElement | None
    tail: QueueElement | None


def create_new_queue():
    return Queue(0, None, None)


def is_empty(queue):
    return queue.size == 0


def get_size(queue):
    return queue.size


def top(queue):
    if not is_empty(queue):
        return queue.head.value
    return None


def last(queue):
    if not is_empty(queue):
        return queue.tail.value
    return None


def push(queue, value):
    element = QueueElement(value, None)

    if is_empty(queue):
        queue.head = element

    elif queue.size == 1:
        queue.tail = element
        queue.head = QueueElement(queue.head.value, queue.tail)

    else:
        queue.tail = QueueElement(value, element)
        queue.tail = element

    queue.size += 1


def pop(queue):
    if not is_empty(queue):
        queue.head = queue.head.next
        queue.size -= 1
