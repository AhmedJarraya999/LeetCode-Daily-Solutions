class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        
        for k in range(n-1, 1, -1):   # fix the largest side
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += (j - i)   # all pairs between i and j are valid
                    j -= 1
                else:
                    i += 1
        return res