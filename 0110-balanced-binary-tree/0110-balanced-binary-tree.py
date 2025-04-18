class Solution(object):
    def isBalanced(self, root):
        def check (node):
            if not node:
                return 0
            left=check(node.left)
            if left==-1:
                return -1

            right= check(node.right)
            if right==-1:
                return -1

            if abs(left-right)>1:
                return -1
            return max(left,right)+1
            
        return check(root) != -1
