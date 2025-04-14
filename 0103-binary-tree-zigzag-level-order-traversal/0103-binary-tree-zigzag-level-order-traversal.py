# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        odd=False
        if not root:
            return []
        result=[]
        queue=deque([root])
        while queue:
            level=[]
            for _ in range(len(queue)):  # process all nodes at this level  
             node = queue.popleft()  
             level.append(node.val)  
             if odd==True:
                if node.left:
                   queue.append(node.left)
                if node.right:
                   queue.append(node.right) 
             else:
                if node.right:
                   queue.append(node.right) 
                if node.left:
                   queue.append(node.left)
            result.append(level)
            odd= not odd
        return result
                
              
            

        