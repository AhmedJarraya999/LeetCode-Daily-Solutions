class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt=0
        left,right=0,0
        bestsofar=0
        for right in range(len(nums)):
            if nums[right]==0:
                cnt+=1
            while cnt>k:
                if nums[left]==0:
                    cnt-=1
                left+=1
            bestsofar=max(bestsofar,right-left+1)
        return bestsofar
        