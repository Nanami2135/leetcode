# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        v_max = 0

        def maxValue(node: Optional[TreeNode], max_anc, min_anc):

            if node is None:
                return 0

            nonlocal v_max

            v = max(abs(node.val - max_anc), abs(node.val - min_anc))
            v_max = max(v_max, v)
            
            max_anc = max(node.val, max_anc)
            min_anc = max(node.val, min_anc)

            maxValue(node.left, max_anc, min_anc)
            maxValue(node.right, max_anc, min_anc)
        
        maxValue(root.left, root.val, root.val)
        maxValue(root.right, root.val, root.val)

        return v_max


        
        