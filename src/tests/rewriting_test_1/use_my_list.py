from src.tests.rewriting_test_1.rewriting_test1_task2 import *

if __name__ == "__main__":
    test_list = create_new_list()
    for i in range(1, 11):
        insert(test_list, i)

    print(f"Top element queue: {list_head(test_list)}")
    print(f"Last element queue: {list_tail(test_list)}")
    print(f"Locate 5: {locate(test_list, 5)}")
    print(f"Element on 6 position: {retrieve(test_list, 6)}")
