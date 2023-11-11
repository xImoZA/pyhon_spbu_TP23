from dataclasses import dataclass
from collections import namedtuple

ListElement = namedtuple("ListElement", ["value", "next"])


@dataclass
class List:
    size: int
    head: ListElement
    tail: ListElement


def create_new_list():
    return List(0, None, None)


def empty(my_list):
    return my_list.size == 0


def list_head(my_list):
    if not empty(my_list):
        return my_list.head.value
    return None


def list_tail(my_list):
    if not empty(my_list):
        return my_list.tail.value
    return None


def insert(my_list, value):
    if value is not None:
        element = ListElement(value, None)

        if empty(my_list):
            my_list.head = element

        elif my_list.size == 1:
            my_list.tail = element
            my_list.head = ListElement(my_list.head.value, my_list.tail)

        else:
            my_list.tail = ListElement(value, element)
            my_list.tail = element

        my_list.size += 1
        return True
    return False


def locate(my_list, value):
    if not empty(my_list):
        now_element = my_list.head
        position = 1

        while value != now_element.value:
            now_element = now_element.next
            position += 1

        if now_element.value == value:
            return position

    return None


def retrieve(my_list, value):
    if not empty(my_list):
        now_element = my_list.head
        position = 1

        while position != value:
            now_element = now_element.next
            position += 1

        if position == value:
            return now_element.value

    return None


# def delete(my_list, value):
#     if not empty(my_list):
#         now_element = my_list.head
#         position = 1
#         while position + 1 != value:
#             now_element = now_element.next
#             position += 1
#
#         if position + 1 == value:
#             now_element = ListElement(value, now_element.next.next)
#             return True
#
#     return False
# я не успела (((
