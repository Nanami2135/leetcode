# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def maxNode(root: Optional[TreeNode], max_node: int) -> int:
            if root is None:
                return 0
            
            if root.val >= max_node:
                max_node = root.val
                return maxNode(root.left, max_node) + maxNode(root.right, max_node) + 1
            else:
                return maxNode(root.left, max_node) + maxNode(root.right, max_node)
        
        return maxNode(root, root.val)  
