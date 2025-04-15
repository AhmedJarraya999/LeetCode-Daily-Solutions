# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        cur1,stack1=p,[]
        res1=[]
        res2=[]
        cur2,stack2=q,[]

        while cur1 or stack1:
            if cur1:
                res1.append(cur1.val)
                stack1.append(cur1.right)
                cur1=cur1.left
            else:
                res1.append(None)   #marker
                cur1=stack1.pop()
        while cur2 or stack2:
            if cur2:
                res2.append(cur2.val)
                stack2.append(cur2.right)
                cur2=cur2.left
            else:
                res2.append(None) #marker
                cur2=stack2.pop()
        if res1==res2:
            return True
        else: 
            return False