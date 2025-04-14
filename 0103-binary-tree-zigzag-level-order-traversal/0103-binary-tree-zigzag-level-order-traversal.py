# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        odd=True 
        if not root:
            return []
        result=[]
        queue=deque([root])
        while queue:
            level=[]
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)    
            if not odd:
                level.reverse()
            result.append(level)
            odd= not odd
        return result
                
              
            

        