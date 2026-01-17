class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Areas of individual rectangles
        areaA = (ax2 - ax1) * (ay2 - ay1)
        areaB = (bx2 - bx1) * (by2 - by1)
        
        # Overlap rectangle
        overlap_left   = max(ax1, bx1)
        overlap_bottom = max(ay1, by1)
        overlap_right  = min(ax2, bx2)
        overlap_top    = min(ay2, by2)
        
        # Overlap area
        overlap_area = 0
        if overlap_right > overlap_left and overlap_top > overlap_bottom:
            overlap_area = (overlap_right - overlap_left) * (overlap_top - overlap_bottom)
        
        # Total area = A + B - overlap
        return areaA + areaB - overlap_area