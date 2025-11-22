from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            modulo = num % 3
            if modulo != 0:
                res += min(modulo, 3 - modulo)
        return res
