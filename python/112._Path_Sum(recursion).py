# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathSum(root: Optional[TreeNode], targetSum: int, prevSum: int) -> bool:
            if root is None:
                return False
            if root.left is None and root.right is None:
                curSum = prevSum + root.val
                return targetSum == curSum
            
            return pathSum(root.left, targetSum, curSum) or pathSum(root.right, targetSum, curSum)
        
        return pathSum(root, targetSum, 0)
