# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = curr = head

        count = 0

        while curr:
            count += 1
            curr = curr.next
        
        idx = count - n

        curr = dummy
        prev = head
        i = 0
        if i == idx:
            return dummy.next
        while i != idx:
            prev = curr
            curr = curr.next
            i+=1
        
        temp = curr.next
        prev.next = temp

        return dummy


        
