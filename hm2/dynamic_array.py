
import ctypes                                      # provides low-level arrays

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def getsize(self):
        import sys
        try:
            return sys.getsizeof(self._A)
          
        except:
            return 0
    def ToString(self):
        try:
            for i in self._A:
                print(i," ")
        except:
            pass
    
    def getLength(self):
        return len(self._A)
    def __init__(self):
        """Create an empty array."""
        self._n = 0                                    # count actual elements
        self._capacity = 1                             # default array capacity
        self._A = self._make_array(self._capacity)     # low-level array
    def _make_array(self, c):                        # nonpublic utitity
        """Return new array with capacity c."""  
        return (c * ctypes.py_object)()               # see ctypes documentation
    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:                 # not enough room
            self._resize(2 * self._capacity)             # so double capacity
        self._A[self._n] = obj
        self._n += 1
    def _resize(self, c):                            # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)                        # new (bigger) array
        print(" şu an amortized cost işlemi ... ")
        for k in range(self._n):                       # for each existing value
            B[k] = self._A[k]
            print(" şu an move işlemi ... ")
        self._A = B                                    # use the bigger array
        self._capacity = c

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n
    def len_n(self):
        """Return number of elements stored in the array."""
        return self._n
    
    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]                              # retrieve from array
    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:                  # not enough room
            self._resize(2 * self._capacity)             # so double capacity
        for j in range(self._n, k, -1):                # shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value                             # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:              # found a match!
                for j in range(k, self._n - 1):    # shift others to fill gap
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None        # help garbage collection
                self._n -= 1                       # we have one less item
        return                             # exit immediately
        raise ValueError('value not found')    # only reached if no match

c=DynamicArray()
print(c.getLength(), c.getsize())

c=DynamicArray()
for i in range(150):
    c.append(-100)
print(c.getLength(), c.getsize(),c.len_n())


import sys
from pympler import asizeof

s_1=sys.getsizeof(c)
s_2=asizeof.asizeof(c)
print("s_1 : {0}, s_2 : {1}".format(s_1,s_2))

print(get_size(c))

n=1000000
for i in range(n):
    c.append(12)
    c.append("sdfsdfsdf")

s_1 = sys.getsizeof(c)
s_2 = asizeof.asizeof(c)
print("n s_1 : {0}, s_2 : {1}".format(s_1, s_2))

print(c._A)

c=DynamicArray()
for i in range(10):
    c.append(i)
    # c.ToString()
print("len : {0}".format(c.getLength()),end=" ")
print("size : {0}".format(c.getsize()))

for i in range(10000):
    c.append(i)
    # c.ToString()
print("len : {0}".format(c.getLength()),end=" ")
print("size : {0}".format(c.getsize()))

print(get_size(c))


def testDynamicArray(n=100):
      
  for i in range(n):
    c.append(12)
    c.append("sdfsdfsdf")

  s_1 = sys.getsizeof(c)
  s_2 = asizeof.asizeof(c)
  print("n s_1 : {0}, s_2 : {1}".format(s_1, s_2))

  for i in range(n*10):
    c.append(12)
    c.append("sdfsdfsdf")
  s_1 = sys.getsizeof(c)
  s_2 = asizeof.asizeof(c)
  print("n*10  s_1 : {0}, s_2 : {1}".format(s_1, s_2))

  for i in range(n*100):
    c.append(12)
    c.append("sdfsdfsdf")
  s_1 = sys.getsizeof(c)
  s_2 = asizeof.asizeof(c)
  print("n*100  s_1 : {0}, s_2 : {1}".format(s_1, s_2))
# testDynamicArray(1000)
c=DynamicArray();
for i in range(10):
  c.append(i)
  c.ToString()
  print("len : {0}".format(c.getLength()))
  print("size : {0}".format(c.getsize()))


  import sys

def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size
