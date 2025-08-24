class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen={}
        right,left=0,0
        cur_sum=0
        bestsofar=0
        for right,num in enumerate(nums):
            while num in seen and seen[num]>=left:
                    cur_sum-=nums[left]
                    del seen[nums[left]]
                    left+=1

            seen[num]=right
            cur_sum+=num
            while right-left+1>k:
                cur_sum-=nums[left]
                del seen[nums[left]]
                left+=1
            if right-left+1==k:
                bestsofar=max(cur_sum,bestsofar)
        return bestsofar


