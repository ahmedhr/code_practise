# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    inorder-traversal - Leetcode
    """
    def inorderTraversal(self, node: TreeNode) -> List[int]:
        ans = []
        stack = [node]
        if node:
            while stack:
                if node and node.left:
                    stack.append(node.left)
                    node = node.left
                    continue
                node = stack.pop()
                ans.append(node.val)
                node = node.right
                if node:
                    stack.append(node)
        return ans





