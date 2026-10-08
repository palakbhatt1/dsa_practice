# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        
        curr = head
        count = 0

        while curr!=None:

            count +=1
            curr = curr.next

        power = count - 1

        curr = head
        sol = 0

        while curr!= None:

            sol += curr.val * (2 ** power)

            power -= 1

            curr = curr.next

        return sol


