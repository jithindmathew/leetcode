# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        elements = []
        
        if root is None:
            return elements
        else:
            elements.append(root.val)
        
        if root.left:
            elements += self.preorderTraversal(root.left)
            
        if root.right:
            elements += self.preorderTraversal(root.right)
        return elements
        