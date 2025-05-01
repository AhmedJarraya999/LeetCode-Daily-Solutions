class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[nums[i]]=i

        