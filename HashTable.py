from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ TODO: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    myList = []

    for i in range(self.size):
      myList.append(LinkedList())

    return myList




  # 2️⃣ TODO: Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    first_letter = key[0].lower()
    distance_from_a = ord(first_letter) - ord('a')
    index = distance_from_a % self.size

    return index




  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the 
  # key is the word and the value is a counter for the number of times the word appeared. 
  # When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    new_data = (key, value)
    arr_index = self.hash_func(new_data[0])
    linked_list = self.arr[arr_index]
    linked_list_index = linked_list.find(new_data[0])

    print(f'Looking for: {new_data[0]} in [{arr_index}]')

    if linked_list_index == -1:
      linked_list.append(new_data)
    else:
      print(f'Duplicate: {new_data[0]}')
      linked_list.update_node(key)


  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    for linked_list in self.arr:
      linked_list.print_nodes()



