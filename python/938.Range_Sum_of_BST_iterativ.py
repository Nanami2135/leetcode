# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:
            return 0
        
        stack = [root]

        result = 0

        while stack:

            node = stack.pop()

            if node.val >= low and node.val <= high:
                result += node.val

            if node.val > low and node.left is not None:
                stack.append(node.left)

            if node.val  is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            
            if node.val < low:
                if node.right is not None: 
                    stack.append(node.right)
            
            if node.val > high:
                if node.right is not None: 
                    stack.append(node.left)
        
        return result

            
            

# class Solution:
#     def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#         if not root:
#             return 0
#
#         stack = [root]
#         result = 0
#
#         while stack:
#             node = stack.pop()
#
#             if node.val >= low and node.val <= high:
#                 result += node.val
#
#             if node.val > low and node.left is not None:
#                 stack.append(node.left)
#             if node.val < high and node.right is not None:
#                 stack.append(node.right)
#
#         return result
#
