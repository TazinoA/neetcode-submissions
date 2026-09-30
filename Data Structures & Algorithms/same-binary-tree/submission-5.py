# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = deque([q]), deque([p])

        while q1 and q2:
            currP = q1.popleft()
            currQ = q2.popleft()
            if currP is None and currQ is None:
                continue
            if not currP or not currQ or currP.val != currQ.val:
                return False
            q1.append(currP.left)
            q1.append(currP.right)
            q2.append(currQ.left)
            q2.append(currQ.right)
        return q1 == q2
