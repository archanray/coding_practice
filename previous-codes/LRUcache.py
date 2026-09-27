class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict_ = {}

    def get(self, key):
        if key not in self.dict_:
            return -1
        self.dict_[key] = self.dict_.pop(key)
        return self.dict_[key]

    def put(self, key, value):
        if key in self.dict_:
            self.dict_.pop(key)
        else:
            if self.capacity:
                self.capacity -= 1
            else:
                self.dict_.pop(next(iter(self.dict_)))
        self.dict_[key] = value

obj = LRUCache(5)
print(obj.get(5))