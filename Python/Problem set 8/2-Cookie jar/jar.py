class Jar:
 def __init__(self, capacity=12):
  self._capacity = capacity
  self._size = 0

 def __str__(self):
       return self.size * '🍪'

 def deposit(self, n):
       if n > self.capacity or (self.size + n) > self.capacity:
        raise ValueError('Too many')
 def withdraw(self, n):
        self._size -= n
        if self._size < 0:
            raise ValueError('Invalid Capacity')

 @property
 def capacity(self):
        return (self._capacity)

 @property
 def size(self):
        return (self._size)

 @capacity.setter
 def capacity(self,capacity):
  self._capacity = capacity

 @size.setter
 def size(self,size):
  self._size = size