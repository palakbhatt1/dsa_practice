class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        max_w = 0

        left = 0
        right = len(height) - 1


        while left < right:
    
                dist = abs(left - right)
                water = dist * min(height[left], height[right])
                max_w = max(water, max_w)

                if height[left] < height[right]:
                    left += 1

                else:
                    right -= 1

        return max_w