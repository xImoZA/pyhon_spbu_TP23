from typing import Any


def is_correct_args(array: list[Any]) -> bool:
    for elem in array:
        if not isinstance(elem, type(array[0])):
            return False

    try:
        array[0] < array[1]
        return True

    except TypeError:
        return False


def merge(left: list[Any], right: list[Any]) -> list[Any]:
    i = j = k = 0
    sort_array = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sort_array.append(left[i])
            i += 1
        else:
            sort_array.append(right[j])
            j += 1
        k += 1

    while i < len(left):
        sort_array.append(left[i])
        i += 1
        k += 1

    while j < len(right):
        sort_array.append(right[j])
        j += 1
        k += 1

    return sort_array


def merge_sort(array: list[Any]) -> list[Any]:
    if len(array) > 1:
        left = merge_sort(array[: len(array) // 2])
        right = merge_sort(array[len(array) // 2 :])

        return merge(left, right)

    return array


def sort(array: list[Any]) -> list[Any]:
    if is_correct_args(array):
        return merge_sort(array)

    raise ValueError("Incorrect arguments were passed")
