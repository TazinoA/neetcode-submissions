# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 and l2:
            sumVal = l1.val + l2.val + carry
            if sumVal < 10:
                tail.next = ListNode(sumVal)
                carry = 0
            else:
                tail.next = ListNode(sumVal%10)
                carry = sumVal // 10
            l1, l2, tail = l1.next, l2.next, tail.next
        while l1:
            sumVal = l1.val + carry
            if sumVal < 10:
                tail.next = ListNode(sumVal)
                carry = 0
            else:
                tail.next = ListNode(sumVal%10)
                carry = sumVal // 10
            l1, tail = l1.next, tail.next
        while l2:
            sumVal = l2.val + carry
            if sumVal < 10:
                tail.next = ListNode(sumVal)
                carry = 0
            else:
                tail.next = ListNode(sumVal%10)
                carry = sumVal // 10
            l2, tail = l2.next, tail.next
        if carry > 0:
            tail.next = ListNode(carry)
        
        
        return dummy.next