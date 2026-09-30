# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
    1
   / \
      2
       \
        3
0
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def nodeHeight(node):
            if not node:
                return 0
            return 1+max(nodeHeight(node.left), nodeHeight(node.right))
        
        if abs(nodeHeight(root.left) - nodeHeight(root.right)) > 1:
            return False
        
        return self.isBalanced(root.right) and self.isBalanced(root.left)