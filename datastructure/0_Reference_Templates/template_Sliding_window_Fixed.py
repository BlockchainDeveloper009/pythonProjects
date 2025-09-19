from collections import defaultdict

class SlidingWindow:
    def find_max_average_brute_force(self, nums, k):
        max_avg = float('-inf')

        for i in range(len(nums) - k + 1):
            max_avg = max(max_avg, sum(nums[i:i + k]) / k)

        return max_avg

    def find_max_average_sliding_window_11(self, nums, k):
        sum_window = sum(nums[:k])
        max_sum = sum_window

        for i in range(k, len(nums)):
            sum_window += nums[i] - nums[i - k]
            max_sum = max(max_sum, sum_window)

        return max_sum // k

    """
    A B C D B E A
    """

    def length_of_longest_substring_sliding_window_11(self, s):
        seen = set()
        max_length = left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)
        #  4 = max(4, 4 - 2 + 1) 4
        #  4 = max(4, 3)  - cdb(3)
        return max_length
    """
    below prob is solved in freecodecamp  dsa
    """
    def length_of_longest_substring_sliding_window_12(self, s):
        longest = 0
        l = 0
        counter: dict[str, int] = defaultdict(int)
        for r in range(len(s)):
            counter[s[r]] +=1
            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l+=1
            longest = max(longest, r - 1 +1)
        return longest


        return max_length

    def length_of_longest_substring_sliding_window_frequency_array(self, s):
        freq = [0] * 128
        max_length = left = 0

        for right in range(len(s)):
            freq[ord(s[right])] += 1

            while freq[ord(s[right])] > 1:
                freq[ord(s[left])] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

    def subarray_sum_fixed_11(self , nums, k):
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        largest = window_sum
        for right in range(k, len(nums)):
            left = right - k
            window_sum -= nums[left]
            window_sum += nums[right]
            largest = max(largest, window_sum)
        return largest


s = SlidingWindow()
nums = [1,2,3,7,4,1]
k =3
expected = 14
print(s.find_max_average_sliding_window_11(nums,k))

# if __name__ == "main":
#     nums = [int(x) for x in input().split()]
#     k = int(input())
#     print(s.find_max_average_sliding_window(nums,k))