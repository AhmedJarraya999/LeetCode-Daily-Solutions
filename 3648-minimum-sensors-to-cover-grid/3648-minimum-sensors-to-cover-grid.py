class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        side = 2 * k + 1
        rows = math.ceil(n / side)
        cols = math.ceil(m / side)
        return rows * cols
        
        