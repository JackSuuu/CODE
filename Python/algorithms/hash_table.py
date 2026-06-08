

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None for _ in range(self.size)]
        self.data = [None for _ in range(self.size)]

    def put(self, key, data):
        hash_val = self.hash_function(key, len(self.slots))

        # 正常情况
        if self.slots[hash_val] is None:
            self.slots[hash_val] = key
            self.data[hash_val] = data
        # collision 发生处理
        else:
            if self.slots[hash_val] == key:
                self.data[hash_val] = data  # Replace
            else:
                next_slot = self.rehash(hash_val, len(self.slots))
                while (self.slots[next_slot] is not None) and (self.slots[next_slot] != key):
                    next_slot = self.rehash(next_slot, len(self.slots))  # Keep rehash()

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def rehash(old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while (self.slots[position] is not None) and (not found) and (not stop):
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    # 实现索引操作
    def __getItem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


MyTable = HashTable()
MyTable[54] = "cat"
print(MyTable.__getItem__(54))

MyTable[50] = "cat"
print(MyTable.__getItem__(54))

print(MyTable.slots)
print(MyTable.data)
