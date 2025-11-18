class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2 * n):
            num = nums[i % n]

            while stack and nums[stack[-1]] < num:
                index = stack.pop()
                ans[index] = num

            if i < n:  # only push the first pass
                stack.append(i)

        return ans