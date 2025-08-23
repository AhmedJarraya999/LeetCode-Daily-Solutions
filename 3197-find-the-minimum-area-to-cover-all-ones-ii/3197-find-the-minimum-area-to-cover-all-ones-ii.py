from typing import List

class Solution:
    def __init__(self):
        self.pref = []

    def computePrefixSum(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        # pref is (m+1) x (n+1)
        self.pref = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.pref[i+1][j+1] = grid[i][j] + self.pref[i+1][j] + self.pref[i][j+1] - self.pref[i][j]

    def getBoxSum(self, x1: int, x2: int, y1: int, y2: int) -> int:
        if x1 > x2 or y1 > y2:
            return 0
        return self.pref[x2+1][y2+1] - self.pref[x1][y2+1] - self.pref[x2+1][y1] + self.pref[x1][y1]

    def findBoundingCoordinates(self, grid: List[List[int]]):
        m, n = len(grid), len(grid[0])
        low_x, high_x = float('inf'), -1
        low_y, high_y = float('inf'), -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    low_x = min(low_x, i)
                    high_x = max(high_x, i)
                    low_y = min(low_y, j)
                    high_y = max(high_y, j)
        if high_x == -1:
            return None
        return (low_x, high_x, low_y, high_y)

    def findMinArea(self, x1: int, x2: int, y1: int, y2: int, grid: List[List[int]]) -> int:
        if x1 > x2 or y1 > y2:
            return 0
        total = self.getBoxSum(x1, x2, y1, y2)
        if total == 0:
            return 0

        # find min_x
        min_x = x2
        lo, hi = x1, x2
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.getBoxSum(x1, mid, y1, y2) > 0:
                min_x = mid
                hi = mid - 1
            else:
                lo = mid + 1

        # find max_x
        max_x = x1
        lo, hi = x1, x2
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.getBoxSum(mid, x2, y1, y2) > 0:
                max_x = mid
                lo = mid + 1
            else:
                hi = mid - 1

        # find min_y
        min_y = y2
        lo, hi = y1, y2
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.getBoxSum(x1, x2, y1, mid) > 0:
                min_y = mid
                hi = mid - 1
            else:
                lo = mid + 1

        # find max_y
        max_y = y1
        lo, hi = y1, y2
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.getBoxSum(x1, x2, mid, y2) > 0:
                max_y = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return (max_x - min_x + 1) * (max_y - min_y + 1)

    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.computePrefixSum(grid)

        bounds = self.findBoundingCoordinates(grid)
        if bounds is None:
            return 0
        low_x, high_x, low_y, high_y = bounds

        lowest_area = float('inf')

        # Case 1..4
        for i in range(low_x, high_x):
            for j in range(low_y, high_y):
                for count in range(1, 5):
                    if count == 1:
                        area = ( self.findMinArea(low_x, i, low_y, j, grid)
                               + self.findMinArea(low_x, i, j+1, high_y, grid)
                               + self.findMinArea(i+1, high_x, low_y, high_y, grid) )
                    elif count == 2:
                        area = ( self.findMinArea(low_x, high_x, low_y, j, grid)
                               + self.findMinArea(low_x, i, j+1, high_y, grid)
                               + self.findMinArea(i+1, high_x, j+1, high_y, grid) )
                    elif count == 3:
                        area = ( self.findMinArea(low_x, i, low_y, high_y, grid)
                               + self.findMinArea(i+1, high_x, low_y, j, grid)
                               + self.findMinArea(i+1, high_x, j+1, high_y, grid) )
                    else: # count == 4
                        area = ( self.findMinArea(low_x, i, low_y, j, grid)
                               + self.findMinArea(i+1, high_x, low_y, j, grid)
                               + self.findMinArea(low_x, high_x, j+1, high_y, grid) )
                    lowest_area = min(lowest_area, area)

        # Case-5: Horizontal slicing
        for i in range(low_x, high_x - 1):
            for j in range(i+1, high_x):
                area = ( self.findMinArea(low_x, i, low_y, high_y, grid)
                       + self.findMinArea(i+1, j, low_y, high_y, grid)
                       + self.findMinArea(j+1, high_x, low_y, high_y, grid) )
                lowest_area = min(lowest_area, area)

        # Case-6: Vertical slicing
        for i in range(low_y, high_y - 1):
            for j in range(i+1, high_y):
                area = ( self.findMinArea(low_x, high_x, low_y, i, grid)
                       + self.findMinArea(low_x, high_x, i+1, j, grid)
                       + self.findMinArea(low_x, high_x, j+1, high_y, grid) )
                lowest_area = min(lowest_area, area)

        return 0 if lowest_area == float('inf') else int(lowest_area)