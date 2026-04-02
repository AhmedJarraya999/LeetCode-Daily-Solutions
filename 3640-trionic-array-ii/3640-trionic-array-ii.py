from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        
        pref = [0] * n
        suff = [0] * n
        
        # pref: max increasing subarray sum ending at i
        pref[0] = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                pref[i] = max(pref[i - 1] + nums[i], nums[i])
            else:
                pref[i] = nums[i]
        
        # suff: max increasing subarray sum starting at i
        suff[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                suff[i] = max(suff[i + 1] + nums[i], nums[i])
            else:
                suff[i] = nums[i]
        
        res = float('-inf')
        i = 2
        
        while i < n - 1:
            if nums[i] < nums[i - 1]:
                temp = nums[i - 1]
                x = i - 2
                
                # decreasing segment
                while i < n - 1 and nums[i] < nums[i - 1]:
                    temp += nums[i]
                    i += 1
                
                # check valid trionic shape
                if nums[i] > nums[i - 1] and nums[x] < nums[x + 1]:
                    res = max(res, temp + pref[x] + suff[i])
            else:
                i += 1
        
        return res