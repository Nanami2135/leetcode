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

        sum_nodes = 0
        new_low = root.left
        new_high = root.right

        def sumNode(root: Optional[TreeNode]) -> None :
            
            nonlocal sum_nodes
            nonlocal new_low
            nonlocal new_high

            if not root:
                return 0
            
            if root.val >= low and root.val <= high:
                sum_nodes += root.val

            if root.val < low and root.right is not None:
                if root.right.val < low:
                    return 0
                else:
                    sumNode(root.right)
            
            if root.val > high and root.left is not None:
                if root.left.val > high:
                    return 0
                else: sumNode(root.right)
            sumNode(root.left)
            sumNode(root.right)

        sumNode(root)

        return sum_nodes

            