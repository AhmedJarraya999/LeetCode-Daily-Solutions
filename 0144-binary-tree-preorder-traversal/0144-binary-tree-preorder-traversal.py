
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        cur,stack= root,[]
        res = []

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur=cur.left
            else:
                cur=stack.pop()
        return res



        