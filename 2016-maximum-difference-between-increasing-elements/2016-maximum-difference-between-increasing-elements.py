class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val=nums[0]
        max_diff=-1
        for num in nums[1:]:
            if num>min_val:
                max_diff=max(num-min_val,max_diff)
            else:
                min_val=min(min_val,num)
        return max_diff

            

        