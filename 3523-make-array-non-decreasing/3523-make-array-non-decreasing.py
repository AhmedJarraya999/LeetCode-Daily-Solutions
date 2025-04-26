class Solution(object):
    def maximumPossibleSize(self, nums):
        last = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] >= last:
                count += 1
                last = nums[i]
            else:
                last = max(last, nums[i])
        return count
