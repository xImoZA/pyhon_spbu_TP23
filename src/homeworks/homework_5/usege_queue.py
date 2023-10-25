from src.homeworks.homework_5.homework_5_task_3 import *

if __name__ == "__main__":
    test_queue = create_new_queue()
    print(f"Size empty queue: {size(test_queue)}")

    for i in range(1, 11):
        push(test_queue, i)

    print(f"Size queue: {size(test_queue)}")
    print(f"Top element queue: {top(test_queue)}")
    print(f"Last element queue: {last(test_queue)}")

    pop(test_queue)

    print(f"Size new queue: {size(test_queue)}")
    print(f"New top element queue: {top(test_queue)}")
    print(f"Last element queue: {last(test_queue)}")
