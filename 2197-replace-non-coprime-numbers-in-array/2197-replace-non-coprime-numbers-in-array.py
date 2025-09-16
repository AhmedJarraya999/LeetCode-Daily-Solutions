from math import gcd
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            stack.append(num)
            
            # keep merging while top two are non-coprime
            while len(stack) > 1:
                x, y = stack[-2], stack[-1]
                g = gcd(x, y)
                if g == 1:
                    break  # coprime → stop
                lcm = x // g * y  # avoid overflow
                stack.pop()
                stack[-1] = lcm  # replace second top with merged value
                
        return stack
