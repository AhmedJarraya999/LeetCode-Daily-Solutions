from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)

        for i in range(1, n - 1):
            if nums[i] == nums[i - 1]:
                continue

            leftpointer = i - 1
            while leftpointer >= 0 and nums[leftpointer] == nums[i]:
                leftpointer -= 1

            rightpointer = i + 1
            while rightpointer < n and nums[rightpointer] == nums[i]:
                rightpointer += 1

            # Check boundaries
            if leftpointer >= 0 and rightpointer < n:
                if nums[i] > nums[leftpointer] and nums[i] > nums[rightpointer]:
                    cnt += 1  

                elif nums[i] < nums[leftpointer] and nums[i] < nums[rightpointer]:
                    cnt += 1  

        return cnt
