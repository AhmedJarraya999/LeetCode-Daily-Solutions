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
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        def build(left,right):
            if left>right:
                return None
            mid=(left+right)//2
            root=TreeNode(arr[mid])
            root.left=build(left,mid-1)
            root.right=build(mid+1,right)
            return root
        return build(0,len(arr)-1)
        # # Step 1: Inorder traversal to get sorted values
        # def inorder(node):
        #     if not node:
        #         return []
        #     return inorder(node.left) + [node.val] + inorder(node.right)
        
        # # Step 2: Build balanced BST from sorted array
        # def build(nums, l, r):
        #     if l > r:
        #         return None
            
        #     mid = (l + r) // 2
        #     node = TreeNode(nums[mid])
            
        #     node.left = build(nums, l, mid - 1)
        #     node.right = build(nums, mid + 1, r)
            
        #     return node
        
        # nums = inorder(root)
        # return build(nums, 0, len(nums) - 1)