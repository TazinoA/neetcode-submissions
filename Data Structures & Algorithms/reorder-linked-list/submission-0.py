# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        res = []

        while curr:
            res.append(curr)
            curr = curr.next
        
        res.sort(key = lambda node:node.val)

        dummy = curr = ListNode()

        for i in range((len(res)+1)//2):
            curr.next = res[i]
            curr = curr.next
            curr.next = res[len(res)-i-1]
            curr = curr.next
        
        curr.next = None