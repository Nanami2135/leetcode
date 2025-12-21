# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        
        up_tree = [root]
        first = 0
        second = 0

        left_tree = [root.left]
        right_tree = [root.right]

        while up_tree :

            node = up_tree.pop()
            if (node.left.val == p.val and node.right.val == q.val) or (node.right.val == p.val and node.left.val == q.val):
                return node
            
        
            
        
