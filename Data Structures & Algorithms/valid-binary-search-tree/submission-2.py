# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def helper(tree, arr):
            if not tree:
                return
            helper(tree.left, arr)
            arr.append(tree.val)
            helper(tree.right, arr)
        
        res = []
        helper(root, res)
        for i in range(len(res) - 1):
            if res[i+1] <= res[i]:
                return False
        return True
        