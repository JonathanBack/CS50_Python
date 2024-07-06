class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        cookies = "🍪" * self.size
        return f"{cookies}"

    def deposit(self, n):
        if type(n) is int and n >= 0:
            self.size += n
        if self.size > self.capacity:
            raise ValueError

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        if type(n) is int and n >= 0:
            self.size -= n


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0 or type(capacity) is not int:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 and type(size) is not int:
            raise ValueError
        self._size = size

def main():
    ...
if __name__ == "__main__":
    main()
