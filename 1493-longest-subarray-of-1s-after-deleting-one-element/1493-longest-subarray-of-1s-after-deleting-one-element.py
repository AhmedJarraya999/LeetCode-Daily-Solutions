class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left,right=0,0
        bestsofar=0
        zeroes=0
        for right in range(len(nums)):
            #zero louleni 3ibara pointerur right step2
            if nums[right]==0:
                zeroes+=1
            #zero exceed we consider the left pointer to be deleted  step3
            while zeroes>1:
                if nums[left]==0:
                    zeroes-=1
                left+=1
            #par default bech yesxecuti hehdi right betbi3tou ykadem w left bloqué fel 0 step1
            bestsofar=max(bestsofar,right-left)
        return bestsofar

            


        