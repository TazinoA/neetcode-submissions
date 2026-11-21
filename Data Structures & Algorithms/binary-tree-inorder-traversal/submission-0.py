# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(arr, root):
            if not root:
                return arr
            traverse(arr, root.left)
            arr.append(root.val)
            traverse(arr, root.right)
        
        res = []
        traverse(res, root)
        return res