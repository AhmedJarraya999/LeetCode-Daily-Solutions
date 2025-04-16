# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val==val:
            return root
        elif (val<root.val):
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)