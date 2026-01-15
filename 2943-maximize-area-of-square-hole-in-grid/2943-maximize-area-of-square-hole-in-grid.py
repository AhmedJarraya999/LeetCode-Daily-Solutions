class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def max_consecutive_gap(bars):
            bars.sort()
            max_count = count = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    count += 1
                else:
                    count = 1
                max_count = max(max_count, count)
            return max_count + 1
        
        max_h = max_consecutive_gap(hBars)
        max_v = max_consecutive_gap(vBars)
        
        side = min(max_h, max_v)
        return side * side

        