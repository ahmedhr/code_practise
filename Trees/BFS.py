from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Breadth first search AKA Level order traversing using Queue DS
# to find the target value
class Solution:
    @staticmethod
    def findTarget(root: Optional[TreeNode], k: int) -> bool:
        memo = {}
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if k - node.val in memo:
                return True
            memo[node.val] = None
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
