class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):  
            target = num1 - k * num2
            if target < k:  
                continue
            if target >= 0 and bin(target).count("1") <= k <= target:
                return k
        return -1
        