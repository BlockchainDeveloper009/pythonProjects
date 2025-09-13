"""
11. Container With Most Water
Medium
Topics
premium lock iconCompanies
Hint

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # Calculate the current area
            current_width = right - left
            current_height = min(height[left], height[right])
            current_area = current_width * current_height

            # Update the maximum water found so far
            max_water = max(max_water, current_area)

            # Move the pointer pointing to the shorter line inward
            # This is because moving the taller line will not increase the height
            # (as it's limited by the shorter one), but it will decrease the width.
            # Moving the shorter line gives a chance to find a taller line.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water