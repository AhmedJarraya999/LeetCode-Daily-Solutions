class Solution(object):
    def subarraySum(self, nums, k):
        prefixSumMap=defaultdict(int)
        prefixSum=0
        count=0
        prefixSumMap[0] = 1 
        for i in range(len(nums)):
            prefixSum+=nums[i]
            if prefixSum - k in  prefixSumMap:
                count += prefixSumMap[prefixSum - k]
            prefixSumMap[prefixSum]+=1
        return count



