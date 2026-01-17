from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        n = len(points)
        if n <= 2:
            return n
        
        max_points = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 0
            verticals = 0  # special counter for vertical lines
            
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0 and dy == 0:
                    duplicates += 1
                elif dx == 0:
                    verticals += 1  # vertical line
                else:
                    g = gcd(dy, dx)
                    dy //= g
                    dx //= g
                    # Ensure consistent slope representation
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    slopes[(dy, dx)] += 1
            
            current_max = max(slopes.values(), default=0)
            current_max = max(current_max, verticals) + duplicates + 1
            max_points = max(max_points, current_max)
        
        return max_points


# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
#         n=len(points)
#         max_points=0
#         for i in range(n):
#             slopes = defaultdict(int)
#             duplicates=0
#             for j in range(i+1,n):
#                 dx = points[j][0] - points[i][0]
#                 dy=points[j][1]-points[i][1]
#                 if dx==0 and dy==0:
#                     duplicates+=1
#                     continue
#                 # Reduce slope to simplest fraction form
#                 g = gcd(dy, dx)
#                 if g != 0:
#                     dy //= g
#                     dx //= g
                
#                 # Ensure consistent representation for negative slopes
#                 if dx < 0:
#                     dx = -dx
#                     dy = -dy
                
#                 slopes[(dy, dx)] += 1
#              # Max points on a line through points[i]
#             current_max = max(slopes.values(), default=0) + duplicates + 1
#             max_points = max(max_points, current_max)
#         return max_points
            


        