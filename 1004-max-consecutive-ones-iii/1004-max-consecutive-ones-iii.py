class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt=0
        left,right=0,0
        bestsofar=0
        for right in range(len(nums)):
            if nums[right]==0: #this second one
                cnt+=1
            while cnt>k: #this will be step 3 and it will  be bestsoar if appropriate
                if nums[left]==0:
                    cnt-=1
                left+=1
            #by default this will be executed
            bestsofar=max(bestsofar,right-left+1)
        return bestsofar
        