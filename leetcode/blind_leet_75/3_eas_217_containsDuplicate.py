from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False




s = Solution()
test1 = [1,2,3,1]
s.containsDuplicate(test1)
#
# test2 = [1,2,3,4]
# s.containsDuplicate(test2)