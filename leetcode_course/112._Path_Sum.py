# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        stack: list[tuple[TreeNode, int]] = [(root,0)]
        if not root:
            return False

        while stack:
            node,cur_sum  = stack.pop()
            cur_sum += node.val

            if node.left is not None:
                left_tuple = (node.left, cur_sum)
                stack.append(left_tuple)
            if node.right is not None:
                right_tuple = (node.right, cur_sum)
                stack.append(right_tuple)
            if node.right is None and node.left is None:
                if cur_sum == targetSum:
                    return True
        
        return False
            

        
        