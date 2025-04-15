# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isMirror(t1,t2):
            if not t1 and not t2:
                 return True
            if not t1 or not t2:
                return False
            if t1.val!=t2.val:
                return False
            return isMirror(t1.left,t2.right) and isMirror(t1.right,t2.left)
        return isMirror(root.left, root.right)




        if not root:
             return True
        node=root.val
        if node.left!=node.right:
            return False
    
        