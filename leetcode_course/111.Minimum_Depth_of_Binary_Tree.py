# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        result = 100000000000
        stack = [(root,1)]
        while stack is not None:
            node, depth = stack.pop()
            result = min(result,depth)
            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))
            if node.left and node.right is None:
                result = min(result,depth)
        
        return result


        