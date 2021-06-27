class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class lrucache():
    def __init__(self, capacity):
        self.hash_map = dict()
        self.capacity = capacity
        self.head = None
        self.tail = None

    def _addNode(self, new_node):
        key = new_node.key
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        if not self.hash_map.get(key):
            self.hash_map[key] = new_node

    def _deleteNode(self, ex_node):
        key = ex_node.key
        # when a middle element is removed
        if ex_node != self.head and ex_node != self.tail:
            ex_node.prev.next = ex_node.next
            ex_node.next.prev = ex_node.prev
        # when head or tail is removed
        else:
            if self.head == ex_node:
                self.head = self.head.next
                ex_node.next = None
            if self.tail == ex_node:
                self.tail = self.tail.prev
                ex_node.prev = None
        self.hash_map.pop(key)

    def get(self, key):
        if self.hash_map.get(key):
            req_node = self.hash_map[key]
            if req_node != self.head:
                self._deleteNode(req_node)
                self._addNode(req_node)
            return req_node.value
        else:
            return None

    def put(self, key, value):
        new_node = Node(key, value)
        if len(self.hash_map) == self.capacity:
            self._deleteNode(self.tail)
        self._addNode(new_node)


LR = lrucache(5)
LR.put(1, 5)
LR.put(2, 6)
LR.get(1)
LR.put(3, 7)
