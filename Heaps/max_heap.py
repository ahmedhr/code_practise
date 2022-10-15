import math


class Maxheap:
    def __init__(self):
        self.heap_arr = [math.inf]

    def insert(self, num):
        self.heap_arr.append(num)
        last = len(self.heap_arr)
        # Push Up
        # checking if only root is inserted, since infinity is also taken hence checking for 2
        if last == 2:
            return
        last -= 1
        while self.heap_arr[last] > self.heap_arr[last // 2]:
            self.heap_arr[last], self.heap_arr[last // 2] = self.heap_arr[last // 2], self.heap_arr[last]
            last //= 2

    def delete(self):
        last = len(self.heap_arr) - 1
        self.heap_arr[1] = self.heap_arr.pop()
        last -= 1
        curr = i = 1
        max_child = 0
        # Push down
        while i * 2 < last:
            if self.heap_arr[i * 2] > self.heap_arr[(i * 2) + 1]:
                max_child = i * 2
            elif self.heap_arr[(i * 2) + 1] > self.heap_arr[i * 2]:
                max_child = (i * 2) + 1

            if self.heap_arr[max_child] > self.heap_arr[curr]:
                self.heap_arr[max_child], self.heap_arr[curr] = self.heap_arr[curr], self.heap_arr[max_child]
                curr = max_child
                i = max_child


my_heap = Maxheap()
my_heap.insert(9)
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(4)
my_heap.insert(7)
my_heap.insert(8)
my_heap.insert(1)
my_heap.insert(5)
my_heap.insert(9)
my_heap.insert(50)

print(my_heap.heap_arr[1:])
my_heap.delete()

print(my_heap.heap_arr[1:])
my_heap.delete()

print(my_heap.heap_arr[1:])