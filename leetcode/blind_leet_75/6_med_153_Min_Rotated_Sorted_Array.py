"""
153. Find Minimum in Rotated Sorted Array
Medium
Topics
premium lock iconCompanies
Hint

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        # If the array is not rotated (or rotated n times),
        # the first element is the minimum.
        if nums[left] <= nums[right]:
            return nums[left]

        while left <= right:
            mid = left + (right - left) // 2

            # Check if mid is the minimum element
            # This occurs when nums[mid] is smaller than its previous element.
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            # This occurs when mid+1 is the minimum element
            # (i.e., mid is the largest element before the rotation point).
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            # If the left half is sorted, the minimum is in the right half.
            if nums[left] <= nums[mid]:
                left = mid + 1
            # If the right half is sorted, the minimum is in the left half.
            else:
                right = mid - 1

        return -1 # Should not be reached given problem constraints