"""
338. Counting Bits
Easy
Topics
premium lock iconCompanies
Hint

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101



Constraints:

    0 <= n <= 105



Follow up:

    It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
    Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?


"""


class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)  # Initialize an array of size n+1 with zeros

        # Iterate from 1 to n (ans[0] is already 0)
        for i in range(1, n + 1):
            # If i is even, the number of 1's is the same as i // 2
            if i % 2 == 0:
                ans[i] = ans[i // 2]
            # If i is odd, the number of 1's is one more than i // 2
            else:
                ans[i] = ans[i // 2] + 1

        return ans
