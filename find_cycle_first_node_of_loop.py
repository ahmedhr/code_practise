# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        a = None
        if head and head.next:
            
            p1 = head.next
            p2 = head.next.next
            if p1 == p2:
                return p1
            
            while p1 != p2 and (p1 and p2 and p2.next):
                p1 = p1.next
                p2 = p2.next.next
                a = p1

            if not (p1 and p2 and  p2.next):
                a = None
            if a:
                start = head

                while start != a:
                    start = start.next
                    a = a.next
        return a
        