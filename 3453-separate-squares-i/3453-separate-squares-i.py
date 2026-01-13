class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Step 1: Determine search boundaries
        miny = float('inf')
        maxy = float('-inf')
        
        for x, y, l in squares:
            miny = min(miny, y)
            maxy = max(maxy, y + l)

        # Step 2: Function to compute area difference at height mid
        def area_difference(mid):
            below = 0.0
            above = 0.0
            
            for x, y, l in squares:
                # Fully below
                if y + l <= mid:
                    below += l * l
                # Fully above
                elif y >= mid:
                    above += l * l
                # Partially cut
                else:
                    below_height = mid - y
                    above_height = (y + l) - mid
                    below += below_height * l
                    above += above_height * l
            
            return below - above

        # Step 3: Binary search
        left, right = miny, maxy
        eps = 1e-6
        
        while right - left > eps:
            mid = (left + right) / 2
            diff = area_difference(mid)
            
            if diff < 0:
                left = mid
            else:
                right = mid
        
        return (left + right) / 2
