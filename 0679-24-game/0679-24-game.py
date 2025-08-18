from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6  # floating point tolerance

            n = len(nums)
            # try all pairs of numbers
            for i in range(n):
                for j in range(n):
                    if i != j:
                        # create next list excluding i and j
                        next_nums = [nums[k] for k in range(n) if k != i and k != j]
                        # try all operations between nums[i] and nums[j]
                        for op in ['+', '-', '*', '/']:
                            if op == '+':
                                next_nums.append(nums[i] + nums[j])
                            elif op == '-':
                                next_nums.append(nums[i] - nums[j])
                            elif op == '*':
                                next_nums.append(nums[i] * nums[j])
                            elif op == '/':
                                if nums[j] == 0:  # avoid division by zero
                                    continue
                                next_nums.append(nums[i] / nums[j])
                            
                            if solve(next_nums):
                                return True
                            next_nums.pop()  # backtrack
            return False

        # convert cards to float for division
        return solve([float(c) for c in cards])
