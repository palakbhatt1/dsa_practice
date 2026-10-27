# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:


        prev = None
        curr = head

        while curr != None:
            
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head = prev
        curr = head

        if n == 1:
            head = head.next

        else:
            for i in range(n-2):
                curr = curr.next

            curr.next = curr.next.next

        prev = None
        curr = head

        while curr != None:
            
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

        
       



    