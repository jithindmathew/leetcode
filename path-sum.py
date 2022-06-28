# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, summ: int) -> bool:
        
        if not root:
            return False
        
        summ -= root.val
        
        if not root.left and not root.right:
            return summ == 0
        else:
            return self.hasPathSum(root.left, summ) or self.hasPathSum(root.right, summ)
        