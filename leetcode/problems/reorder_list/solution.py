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

        curr = slow.next
        slow.next = None 
        prev = None

        while curr != None:

            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        curr = head

        sec = prev

        while sec != None: 
            next_node = curr.next
            curr.next = sec
            curr = sec
            sec = next_node
