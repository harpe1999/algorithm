
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache=collections.OrderedDict()
        self.capacity=capacity

    # @return an integer
    def get(self, key):
        if not key in self.cache:
            return -1

        value=self.cache.pop(key)
        self.cache[key]=value
        return value


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key]=value
