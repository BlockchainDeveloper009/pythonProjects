"""
371. Sum of Two Integers
Medium
Topics
premium lock iconCompanies

Given two integers a and b, return the sum of the two integers without using the operators + and -.



Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = 2, b = 3
Output: 5



Constraints:

    -1000 <= a, b <= 1000


"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Define a mask for 32-bit integers, as Python handles arbitrary-precision integers
        # but LeetCode often implies 32-bit behavior for bit manipulation problems.
        # This helps in handling negative numbers correctly using two's complement behavior.
        MASK = 0xFFFFFFFF

        # Max value for a 32-bit signed integer
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # Calculate the carry bits: where both bits are 1
            carry = (a & b) & MASK

            # Calculate the sum without carrying: XOR handles bits that are different
            a = (a ^ b) & MASK

            # Shift the carry to the left to add it in the next iteration
            b = (carry << 1) & MASK

        # If the result 'a' is a negative number (exceeds MAX_INT),
        # convert it back from its 32-bit two's complement representation
        # to Python's standard negative integer representation.
        if a > MAX_INT:
            return ~(a ^ MASK)
        else:
            return a
