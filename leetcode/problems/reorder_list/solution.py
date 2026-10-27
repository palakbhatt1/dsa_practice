# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:

        slow = head
        fast = head

        while fast != None and fast.next != None:

            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr != None:

            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        t1 = head
        t2 = prev

        while t2 != None:

            m1 = t1.next
            m2 = t2. next

            t1.next = t2
            t2.next = m1

            t1 = m1
            t2 = m2


        


