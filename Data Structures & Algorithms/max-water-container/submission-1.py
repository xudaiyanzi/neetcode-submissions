class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        max_water = 0

        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            water = h * w

            max_water = max(max_water, water)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_water