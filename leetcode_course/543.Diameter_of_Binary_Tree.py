# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_path = 0
        
        def maxPath(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            nonlocal max_path
            left_path = maxPath(root.left)
            right_path = maxPath(root.right)
            max_path = max(left_path + right_path, max_path)
        
            return max(left_path, right_path) + 1
        
        maxPath(root)
        
        return max_path
