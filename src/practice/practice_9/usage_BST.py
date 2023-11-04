from BST import *

tree = create_tree_map()
print(f"Create a Binary Search Tree. It's traverse: {traverse(tree, 'preorder')}")

put(tree, 4, "*")
put(tree, 2, "+")
put(tree, 1, "x")
put(tree, 3, "y")
put(tree, 6, "-")
put(tree, 5, "w")
put(tree, 7, "z")
print(
    "Add to the root '*' with key 4, '+' with key 2, 'x' with key 1, 'y' with key 3, '-' with key 6, 'w' with key "
    "5, 'z' with key 7"
)

print(f"The value with the {5} key is {get(tree, 5)}")
print(f"Key {3} in the tree? {has_key(tree, 3)}")
print(f"Key {8} in the tree? {has_key(tree, 8)}")

print(f"{traverse(tree, 'postorder')}")
print(
    f"Now tree's preorder traverse: {' '.join(traverse(tree, 'preorder'))}\n"
    f"inorder: {' '.join(traverse(tree, 'inorder'))}\n"
    f"postorder: {' '.join(traverse(tree, 'postorder'))}"
)

remove(tree, 5)
print("Delete 'w'")
print(
    f"Now tree's preorder traverse: {' '.join(traverse(tree, 'preorder'))}\n"
    f"inorder: {' '.join(traverse(tree, 'inorder'))}\n"
    f"postorder: {' '.join(traverse(tree, 'postorder'))}"
)

remove(tree, 6)
print("Delete '-'")
print(
    f"Now tree's preorder traverse: {' '.join(traverse(tree, 'preorder'))}\n"
    f"inorder: {' '.join(traverse(tree, 'inorder'))}\n"
    f"postorder: {' '.join(traverse(tree, 'postorder'))}"
)

delete_tree_map(tree)
print(f"Delete tree. Now it's traverse: {traverse(tree, 'preorder')}")
