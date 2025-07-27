class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second = float('-inf')
        
        for num in reversed(nums):
            if num < second:
                return True
            while stack and num > stack[-1]:
                second = stack.pop()
            stack.append(num)
        
        return False
