class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0

        while i < j:
            # compute current area
            width = j - i
            h = height[i] if height[i] < height[j] else height[j]
            area = h * width
            if area > max_area:
                max_area = area

            # move the pointer at the smaller height inward
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
