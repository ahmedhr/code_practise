# Definition for a binary tree node.
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(val=1,
                left=TreeNode(val=2,
                              left=TreeNode(val=4),
                              right=TreeNode(val=5)),
                right=TreeNode(val=3,
                               left=TreeNode(val=6)))


# Inorder traversal using recursion
# O(n), S(n)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            if root.left:
                res += self.inorderTraversal(root.left)
            if root:
                res += [root.val]
            if root.right:
                res += self.inorderTraversal(root.right)

        return res


# Inorder traversal using stack
# O(n), S(n)
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
                if node := node.right:
                    stack.append(node)
        return ans

# Inorder traversal using Morris Traversal
# https://stackoverflow.com/questions/5502916/explain-morris-inorder-tree-traversal-without-using-stacks-or-recursion
# O(n), S(1)
class Solution:
    @staticmethod
    def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            current = root
            while current is not None:
                if current.left:
                    right_most = current.left
                    while right_most.right is not None:
                        right_most = right_most.right
                    right_most.right = current
                    current = current.left
                    right_most.right.left = None
                else:
                    res.append(current.val)
                    current = current.right
        return res


print(Solution.inorderTraversal(tree))
