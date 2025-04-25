class Solution(object):
    def subarraysDivByK(self, nums, k):
        count=0
        cumSum=0
        remainderMap={0:1}
        for i in range(len(nums)):
            cumSum+=nums[i]
            remainder=cumSum % k
            if remainder not in remainderMap:
                remainderMap[remainder]=1
            else:
                count+=remainderMap[remainder]
                remainderMap[remainder]+=1
        return count


            
    
