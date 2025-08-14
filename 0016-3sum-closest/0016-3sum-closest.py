class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n-2):
            left, right = i + 1, n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                
                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum
                
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    return target  
                    
        return closest_sum
