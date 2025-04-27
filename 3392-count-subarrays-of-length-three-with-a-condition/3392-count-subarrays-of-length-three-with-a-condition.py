class Solution(object):
    def countSubarrays(self, nums):
        count = 0
        for i in range(len(nums) - 2):
            if nums[i+1] % 2 == 0 and nums[i] + nums[i+2] == nums[i+1] / 2:
                count += 1
        return count
