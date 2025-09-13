
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(32):  # Assuming a 32-bit integer
            if (n & 1) == 1:  # Check if the LSB is 1
                count += 1
            n >>= 1  # Right shift n by 1 to check the next bit
        return count

    """
    This more efficient algorithm leverages the property that n & (n - 1) 
    clears the least significant set bit in n. It continues this operation 
    until n becomes 0, counting each time a bit is cleared.
    """
    def hammingWeight_BrianKernighansAlg(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n & (n - 1)  # Clear the least significant set bit
            count += 1
        return count

"""
191. Number of 1 Bits
Easy
Topics
premium lock iconCompanies

Given a positive integer n, write a function that returns the number of

in its binary representation (also known as the Hamming weight).



Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

"""