#
#                    1
#             2               3
#        4        5      6          7


from collections import deque


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


que = deque()

root = Node(val=1,
            left=Node(val=2,
                      left=Node(val=4),
                      right=Node(val=5)),
            right=Node(val=3,
                       left=Node(val=6),
                       right=Node(val=7)))

que.append({1: root})
v = [root.val]
while len(que) > 0:
    current = que.popleft()
    current_level = list(current.keys())[0]
    element = current[current_level]
    next_level = current_level + 1
    print(element.val)
    if current_level % 2 != 0:
        if element.left:
            que.appendleft({next_level: element.left})
            v.append(element.left.val)
        if element.right:
            que.appendleft({next_level: element.right})
            v.append(element.right.val)
    else:
        if element.right:
            que.append({next_level: element.right})
            v.append(element.right.val)
        if element.left:
            que.append({next_level: element.left})
            v.append(element.left.val)

print(v)

# Time complexity O(n)
# Space complexity
# Queue + Stack
# S(n) + S(n) = S(n)
