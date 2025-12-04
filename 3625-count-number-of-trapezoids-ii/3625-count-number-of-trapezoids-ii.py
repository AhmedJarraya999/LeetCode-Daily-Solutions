class Solution:
    def countTrapezoids(self, points):
        from math import gcd
        n = len(points)
        
        # Step 1: map slope → list of segments (each segment is (i,j))
        slopes = {}
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                # normalize direction
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                
                slopes.setdefault((dx, dy), []).append((i, j))
        
        ans = 0
        
        # Step 2: for each slope group, count valid segment pairs
        for segs in slopes.values():
            m = len(segs)
            if m < 2:
                continue
            
            # total segment pairs
            total_pairs = m * (m - 1) // 2
            
            # subtract pairs sharing a common endpoint
            freq = {}
            for a, b in segs:
                freq[a] = freq.get(a, 0) + 1
                freq[b] = freq.get(b, 0) + 1
            
            bad = 0
            for c in freq.values():
                bad += c * (c - 1) // 2
            
            ans += total_pairs - bad
        
        return ans
