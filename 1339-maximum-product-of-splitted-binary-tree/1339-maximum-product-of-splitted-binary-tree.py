# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD=10**9+7
        subtree_sums=[]
        def dfs(node):
            if not node:
                return 0
            left_sum=dfs(node.left)
            right_sum=dfs(node.right)
            subtree_sum=node.val+left_sum+right_sum
            subtree_sums.append(subtree_sum)
            return subtree_sum
        totalSum=dfs(root)
        max_prod = 0
        for s in subtree_sums:
            max_prod = max(max_prod, s * (totalSum - s))
        return max_prod % MOD
            




        