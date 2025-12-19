# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        max_nodes = 0

        stack = [(root,root.val)]

        if root is None:
            return 0
        
        while stack:
            
            node, max_val = stack.pop()

            if node.val >= max_val:
                max_nodes += 1
                max_val = node.val
            if node.left is not None:
                stack.append((node.left, max_val))
            if node.right is not None:
                stack.append((node.right, max_val))
        
        return max_nodes

        

        