# DATA STRUCTURES IN PYTHON

# 1. Lists
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.extend([7, 8])
my_list.insert(2, 99)
my_list.remove(3)
popped = my_list.pop()
index = my_list.index(4)
count = my_list.count(2)
my_list.sort()
my_list.reverse()
copied_list = my_list.copy()
my_list.clear()

# 2. Tuples
tuple1 = (1, 2, 3, 4)
index_tuple = tuple1.index(3)
count_tuple = tuple1.count(2)
tuple2 = tuple1.__add__((5, 6))
print(tuple2.__contains__(6),"tuple2.__contains__(6)")

# 3. Sets
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.update([7, 8])
my_set.remove(2)
my_set.discard(10)
popped_set = my_set.pop()
my_set.clear()

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)
is_subset = set1.issubset(set2)
is_superset = set1.issuperset(set2)

# 4. Dictionaries
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = 4
my_dict.update({'e': 5})
del my_dict['b']
popped_value = my_dict.pop('c')
popped_item = my_dict.popitem()
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
copied_dict = my_dict.copy()
my_dict.clear()

# 5. Deque (from collections)
from collections import deque
my_deque = deque([1, 2, 3])
my_deque.append(4)
my_deque.appendleft(0)
my_deque.pop()
my_deque.popleft()
my_deque.extend([5, 6])
my_deque.extendleft([-1, -2])
my_deque.rotate(2)
my_deque.reverse()
my_deque.clear()

# 6. NamedTuple (from collections)
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age'])
p1 = Person('Alice', 25)
p2 = Person('Bob', 30)
name_p1 = p1.name
age_p2 = p2.age

# 7. DefaultDict (from collections)
from collections import defaultdict
default_dict = defaultdict(int)
default_dict['a'] += 1

# 8. OrderedDict (from collections)
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['x'] = 10
ordered_dict['y'] = 20
ordered_dict['z'] = 30

# 9. Counter (from collections)
from collections import Counter
counter = Counter([1, 2, 2, 3, 3, 3])
most_common = counter.most_common(2)

# 10. Heap (from heapq)
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
smallest = heapq.heappop(heap)
largest = heapq.nlargest(2, heap)
smallest_2 = heapq.nsmallest(2, heap)

# 11. Stack (Using List)
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.pop()

# 12. Queue (Using List)
queue = []
queue.append(100)
queue.append(200)
queue.append(300)
queue.pop(0)

# 13. Queue (Using Queue module)
from queue import Queue
q = Queue()
q.put(1)
q.put(2)
q.put(3)
first = q.get()

# 14. LifoQueue (Stack using Queue module)
from queue import LifoQueue
stack_q = LifoQueue()
stack_q.put(10)
stack_q.put(20)
stack_q.put(30)
top_stack = stack_q.get()

# 15. PriorityQueue
from queue import PriorityQueue
pq = PriorityQueue()
pq.put((2, 'task2'))
pq.put((1, 'task1'))
pq.put((3, 'task3'))
task = pq.get()

# 16. Set

# Using curly braces {}
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
my_set.add(6)  # Adding an element
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Using the set() function
another_set = set([1, 2, 3, 3, 4])
print(another_set)  # Output: {1, 2, 3, 4}

# Creating an empty set
empty_set = set()  # {} creates a dictionary, not a set

# FrozenSet (Immutable set)
frozen_set = frozenset([1, 2, 3, 4])


# 17. String Methods
string = "hello world"
upper_string = string.upper()
lower_string = string.lower()
replaced_string = string.replace("world", "Python")
split_string = string.split()
joined_string = "-".join(split_string)
stripped_string = string.strip()

# 18. ByteArray
byte_arr = bytearray([65, 66, 67])
byte_arr.append(68)

# 19. MemoryView
memory_view = memoryview(byte_arr)
print(memory_view[0], "memory_view[0]")

# 20. Enum (from enum)
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED.name, Color.RED.value)

# 21. Linked List (Custom Implementation)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_list()

