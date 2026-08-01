class MyHashMap:

    def __init__(self):
        self.SIZE = 1000                      # Number of buckets
        self.map = [[] for _ in range(self.SIZE)]

    # Hash Function
    def hash(self, key):
        return key % self.SIZE

    # Insert or Update
    def put(self, key, value):
        index = self.hash(key)
        bucket = self.map[index]

        # Check whether key already exists
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        # Key not found, insert new pair
        bucket.append([key, value])

    # Search
    def get(self, key):
        index = self.hash(key)
        bucket = self.map[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return -1

    # Delete
    def remove(self, key):
        index = self.hash(key)
        bucket = self.map[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return