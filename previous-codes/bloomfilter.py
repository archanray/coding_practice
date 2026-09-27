import math

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bits = [0] * size

    def add(self, element):
        for i in range(self.num_hashes):
            index = hash(element) % self.size
            self.bits[index] = 1

    def contains(self, element):
        for i in range(self.num_hashes):
            index = hash(element) % self.size
            if self.bits[index] == 0:
                return False
        return True

# Example usage:

bloom_filter = BloomFilter(1000, 5)

bloom_filter.add("hello")
bloom_filter.add("world")

print(bloom_filter.contains("hello"))  # True
print(bloom_filter.contains("goodbye"))  # False