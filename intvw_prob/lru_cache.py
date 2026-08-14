"""
LRU Cache:

LRU means Least Recently Used 

How lru works?
Suppose your bookshelf can only hold 3 books.

When you read a book, you place it at the front because it's the most recently used.

If the shelf is full and you want to add a new book, you throw away the book at the back because it hasn't been used for the longest time.

That's exactly what an LRU Cache does. [1,2,3]
"""

class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}

    def get(self,key):
        if key not in self.cache:
            return -1

        value=self.cache.pop(key)
        self.cache[key]=value
        return value

    def put(self,key,value):
        if key in self.cache:
            self.cache.pop(key)

        elif len(self.cache) >= self.capacity:
            old=next(iter(self.cache))
            del self.cache[old]

        self.cache[key]=value


lru = LRUCache(3)

lru.put(1, "A")
lru.put(2, "B")
lru.put(3, "C")

print(lru.cache)

lru.get(2)

print(lru.cache)

lru.put(4, "D")

print(lru.cache)
        
