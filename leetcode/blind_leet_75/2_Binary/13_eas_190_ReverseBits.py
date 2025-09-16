

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Extract the least significant bit of n
            bit = (n >> i) & 1
            # Place the extracted bit in its reversed position in result
            # The i-th bit from the right of n becomes the (31-i)-th bit from the right of result
            result |= (bit << (31 - i))
        return result

"""
190. Reverse Bits
Easy
Topics
premium lock iconCompanies

Reverse bits of a given 32 bits signed integer.

 

Example 1:

Input: n = 43261596

Output: 964176192

Explanation:
Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000

Example 2:

Input: n = 2147483644

Output: 1073741822

Explanation:
Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110
"""