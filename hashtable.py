# HashTable class

class HashTable:

    # Initializes the hashtable with a capacity of 41 and makes all buckets in the list empty.
    # space-time complexity O(1)
    def __init__(self, initial_capacity=41):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # inserts an item into the hashtable as key value pairs
    # space-time complexity O(N)
    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        key_value = [key, value]

        if self.table[bucket] == None:
            self.table[bucket] = list([key_value])
            return True
        else:
            for i in self.table[bucket]:
                if i[0] == bucket:
                    i[1] = value
                    return True
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # space-time complexity O(N)
    def lookup(self, key):
        bucket = hash(key) % len(self.table)
        if self.table[bucket] is not None:
            for i in self.table[bucket]:
                if i[0] == key:
                    return i[1]
        return None

    # updates an item within the hash table or prints an error message if not found.
    # space-time complexity O(N)
    def update(self, key, value):
        bucket = hash(key) % len(self.table)
        if self.table[bucket] is not None:
            for i in self.table[bucket]:
                if i[0] == key:
                    i[1] = value
                    return print(i[1])
        else:
            print("Error updating key")


# testing information
# myHash = HashTable()
# myHash.insert(1, 'Test')
# myHash.insert(5, "randomstuff")
# print(myHash.table)
# # print(myHash.lookup(1))
# # print(myHash.lookup(5))
# # print(myHash.lookup(4))
# print(myHash.update(1, "Correct Test"))
# print(myHash.update(2, "This is an error if I print"))
# print(myHash.table)
