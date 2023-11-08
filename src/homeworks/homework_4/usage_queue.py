from queue import *

if __name__ == "__main__":
    test_queue = create_new_queue()
    print(f"Size empty queue: {get_size(test_queue)}")

    for i in range(1, 11):
        push(test_queue, i)

    print(f"Size queue: {get_size(test_queue)}")
    print(f"Top element queue: {top(test_queue)}")
    print(f"Last element queue: {last(test_queue)}")

    pop(test_queue)

    print(f"Size new queue: {get_size(test_queue)}")
    print(f"New top element queue: {top(test_queue)}")
    print(f"Last element queue: {last(test_queue)}")
