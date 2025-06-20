class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        max_md = 0
        east = west = north = south = 0
        
        for i, c in enumerate(s):
            if c == 'E':
                east += 1
            elif c == 'W':
                west += 1
            elif c == 'N':
                north += 1
            else:  # 'S'
                south += 1
            
            curr_md = abs(east - west) + abs(north - south)
            steps = i + 1
            wasted = steps - curr_md
            
            extra = 0
            if wasted != 0:
                extra = min(2 * k, wasted)
            
            final_curr_md = curr_md + extra
            max_md = max(max_md, final_curr_md)
        
        return max_md
