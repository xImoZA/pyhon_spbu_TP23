from hash_table import *

hash_table = create_hash_table()
print(
    f"Creating a hash table. It's items: {items(hash_table)}, it's size: {hash_table.size}"
)

put(hash_table, "Eren Yeager", "without head")
put(hash_table, "Tony Stark", "dead")
put(hash_table, "Tony Kark", "not exist")
put(hash_table, "Voldemort", "no nose")
print(
    f"Let's add the names of the heroes and their status. Now HashTable's items: {items(hash_table)}, "
    f"it's size: {hash_table.size}"
)

remove(hash_table, "Tony Kark")
print(
    f"Let's remove Tony Kark. Now HashTable's items: {items(hash_table)}, it's size: {hash_table.size}"
)

print(f"Status Voldemort: {get(hash_table, 'Voldemort')}")
print(f"Status Eren Yeager: {get(hash_table, 'Eren Yeager')}")

print(f"Eren Yeager in HashTable? {has_key(hash_table, 'Eren Yeager')}")
print(f"Tony Kark in HashTable? {has_key(hash_table, 'Tony Kark')}")

delete_hash_table(hash_table)
print(
    f"Destroy an instance of the data structure. Now it's items {items(hash_table)}, it's size: {hash_table.size}"
)
