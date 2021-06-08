# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = headA
        B = headB
        intersetval = 0
        ite = 1
        while (ite < 3):
            if A == B:
                intersetval = A
                return intersetval
            aval = A.next
            if aval:
                A = aval
            else:
                A = headB
                ite += 1
            bval = B.next
            if bval:
                B = bval
            else:
                B = headA