#Solution to leet code problem 
#https://leetcode.com/problems/add-two-numbers/


from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mul = 1
        l1_num = l2_num = 0
        while l1 or l2:
            if l1:
                l1_num += l1.val * mul
                l1 = l1.next
            if l2:
                l2_num += l2.val * mul
                l2 = l2.next
            mul *= 10
        rev = (l1_num+l2_num)
        prev_node = None
        initial_node = ListNode()
        while rev:
                last = rev % 10
                if prev_node:
                    next_node = ListNode(last, None)
                    prev_node.next = next_node
                    prev_node = next_node
                else:
                    prev_node = ListNode(last, None)
                    initial_node = prev_node
                rev = rev // 10
        return initial_node