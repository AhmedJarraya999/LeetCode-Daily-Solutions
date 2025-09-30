class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def helper(arr):
            if len(arr)==1:
                return arr[0]
            newArr = [(arr[i] + arr[i+1]) % 10 for i in range(len(arr) - 1)]
            return helper(newArr)
        return helper(nums)
        