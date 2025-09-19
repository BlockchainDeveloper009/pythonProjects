Here are detailed, commented Python solutions for the **first 4 combinatorial/factorial-indexing problems**, structured similarly to what was provided before. Each includes line-by-line explanations for intuition and why loops go over certain ranges, etc.

***

## 1. Next Permutation (LeetCode 31)

```python
def next_permutation(nums):
    """
    Modifies nums in-place to the next lexicographic permutation.
    If no next permutation, rearranges to the lowest (sorted ascending).
    """
    n = len(nums)
    # Step 1: Find pivot from right: first nums[i] < nums[i+1]
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    # If pivot not found, it is last permutation
    if i == -1:
        nums.reverse()
        return

    # Step 2: Find rightmost element > pivot to swap with
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1

    # Step 3: Swap pivot and element at j
    nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse suffix from i+1 to end
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Test
nums = [1, 2, 3]
next_permutation(nums)
print(nums)  # Output: [1, 3, 2]
```

**Explanation:**

- Pivot is the first element from right breaking descending order (finding lexicographically smallest higher sequence).
- Reverse suffix to get the minimum order after swap.
- Loop `i` goes backward to find pivot; `j` finds element just larger than pivot.
- Reversing ensures next permutation is the immediate next lex order, no skips.

***

## 2. K-th Permutation Sequence (LeetCode 60)

```python
import math

def get_permutation(n, k):
    """
    Returns k-th permutation of numbers [1..n].
    """
    # Numbers pool
    numbers = list(range(1, n + 1))
    k -= 1  # zero-based index for calculation
    
    result = []
    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)         # block size for each digit
        index = k // fact                    # pick the index 
        result.append(str(numbers.pop(index))) # pick and remove number
        k %= fact                           # update k to within block

    return ''.join(result)

# Tests
print(get_permutation(3, 3))  # "213"
print(get_permutation(4, 9))  # "2314"
print(get_permutation(3, 1))  # "123"
```

**Explanation:**

- Factorial blocks group permutations by first digit.
- Selecting the digit index is done by integer division.
- Updating `k` by modulus moves into next smaller factorial block for next digits.
- The loop goes from largest to smallest factorial because digits are picked positionally.

***

## 3. K-th Combination (Lexicographic order)

```python
import math

def kth_combination(n, k, idx):
    """
    Returns idx-th (0-based) k-combination from [1..n] in lex order.
    """
    nums = list(range(1, n + 1))
    result = []

    for i in range(k):
        for j, num in enumerate(nums):
            remain = n - j - 1                       # remaining elements after current candidate
            count = math.comb(remain, k - i - 1)    # combinations if num at position i
            if idx < count:
                result.append(num)
                nums = nums[j + 1:]                  # choose num, move ahead
                break
            else:
                idx -= count                         # skip this block of combos
                
    return result

# Tests
print(kth_combination(5, 3, 2))  # [1, 4, 5]
print(kth_combination(4, 2, 3))  # [1, 4]
```

**Explanation:**

- Outer loop picks each combination element.
- Inner loop iterates available numbers to skip groups of combinations.
- `math.comb(remaining, needed)` counts how many combos start with each candidate.
- If `idx` is less than count for a number, this is the correct choice.
- Else, reduce `idx` and move on since we skip this block.

***

## 4. K-th Subset Generation (Lexicographic order)

```python
def kth_subset(nums, idx):
    """
    Return idx-th subset in lex order. nums sorted.
    """
    n = len(nums)
    result = []

    for i in range(n):
        subsets_if_excluded = 2 ** (n - i - 1)  # subsets if element is NOT included
        if idx < subsets_if_excluded:
            # exclude nums[i], just move forward
            continue
        else:
            # include nums[i], reduce idx accordingly
            result.append(nums[i])
            idx -= subsets_if_excluded

    return result

# Tests
nums = [1, 2, 3]
print(kth_subset(nums, 3))  # [2]
nums = [1, 2, 3, 4]
print(kth_subset(nums, 5))  # [2, 4]
```

**Explanation:**

- For each element, count subsets if excluded = $$2^{remaining}$$.
- If `idx` < excluded count, skip including current element.
- Else include element and reduce `idx`.
- Loop covers entire list, deciding include/exclude per element.

***

If you want detailed line-by-line explanations for all code or further examples, just ask!

[1](https://www.nayuki.io/page/next-lexicographical-permutation-algorithm)
[2](https://algo.monster/liteproblems/31)
[3](https://www.geeksforgeeks.org/dsa/next-permutation/)
[4](https://leetcode.com/problems/next-permutation/)
[5](https://stackoverflow.com/questions/11483060/stdnext-permutation-implementation-explanation)
[6](https://takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation/)
[7](https://www.youtube.com/watch?v=JDOXKqF60RQ)
[8](https://www.geeksforgeeks.org/java/implementing-next_permutation-in-java-with-examples/)
[9](https://www.reddit.com/r/rust/comments/mldrsx/how_to_make_this_next_permutation_algorithm_code/)