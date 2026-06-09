# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            # arr.append(node.val)
            arr.append(node)
            inorder(node.right)
        inorder(root)
        def construct(left,right):
            if left>right:
                return None
            mid=(left+right)//2
            root=arr[mid]
            # root=TreeNode(arr[mid])
            root.left=construct(left,mid-1)
            root.right=construct(mid+1,right)
            return root
        return construct(0,len(arr)-1)
            