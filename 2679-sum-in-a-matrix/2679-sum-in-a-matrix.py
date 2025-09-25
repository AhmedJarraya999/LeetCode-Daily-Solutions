class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
      
        for row in nums:
            row.sort()
        
        m, n = len(nums), len(nums[0])
        score = 0

        for j in range(n):
            max_val = 0
            for i in range(m):
                max_val = max(max_val, nums[i][j])
            score += max_val
        
        return score
