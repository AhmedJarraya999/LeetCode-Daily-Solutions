# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD=10**9+7
        max_prod=0
        substrees_sums=[]
        def dfs(node):
            if not node:
                return 0
            left_sum=dfs(node.left)
            right_sum=dfs(node.right)
            cur_sum=node.val+left_sum+right_sum
            substrees_sums.append(cur_sum)
            return cur_sum
        tot_sum=dfs(root)
        for s in substrees_sums:
            max_prod=max(max_prod,(tot_sum-s)*s)
        return max_prod%MOD








        