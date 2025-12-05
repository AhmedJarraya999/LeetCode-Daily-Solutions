class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0
        count = 0
        n = len(nums)
        
        for i in range(n - 1):
            leftSum += nums[i]
            rightSum = totalSum - leftSum
            if leftSum % 2 == rightSum % 2:
                count += 1
                
        return count
        