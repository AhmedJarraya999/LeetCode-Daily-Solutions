class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        lastMin=-1
        lastMax=-1
        badIndex=-1
        count=0
        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                badIndex=i
            if nums[i]==minK:
                lastMin=i
            if nums[i]==maxK:
                lastMax=i
            validStart=min(lastMin,lastMax)
            if validStart>badIndex:
                count+=validStart-badIndex
        return count

        