class Solution(object):
    def findNumbers(self, nums):
        counter=0
        for i in range(len(nums)):
            if len(str(nums[i]))%2==0:
                counter+=1
        return counter
        