"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
first pass:
build map
second pass:
fill in next and random for each node
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        nodeMap = {}

        while curr:
            nodeMap[(curr.val, id(curr))] = Node(curr.val)
            curr = curr.next
        dummy = head
        while dummy:
            curr = nodeMap[(dummy.val, id(dummy))]
            if dummy.next:
                curr.next = nodeMap[(dummy.next.val, id(dummy.next))]
            else:
                curr.next = None
            if dummy.random:
                curr.random = nodeMap[(dummy.random.val, id(dummy.random))]
            else:
                curr.random = None
            dummy = dummy.next
            curr = curr.next

        return nodeMap[(head.val, id(head))]




