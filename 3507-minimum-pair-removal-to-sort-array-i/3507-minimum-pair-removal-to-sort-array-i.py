from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        
        while sorted(nums) != nums:
            besti = 1
            
            # find adjacent pair with minimum sum
            for i in range(2, len(nums)):
                if nums[i] + nums[i - 1] < nums[besti] + nums[besti - 1]:
                    besti = i
            
            new_nums = []
            
            i = 0
            while i < len(nums):
                if i == besti - 1:
                    new_nums.append(nums[i] + nums[i + 1])
                    i += 2
                else:
                    new_nums.append(nums[i])
                    i += 1
            
            nums = new_nums
            ops += 1
        
        return ops
