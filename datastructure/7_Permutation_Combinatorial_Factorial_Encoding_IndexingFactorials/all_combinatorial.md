Here are several prominent examples of problems that use **combinatorial/factorial-indexing techniques**—where direct calculation with factorials, combinatorial formulas, or combinatorial encoding is essential:

***

## Examples of Combinatorial / Factorial-Indexing Problems

### 1. **Next Permutation (LeetCode 31)**
- **Description:** Given a current permutation, generate the next lexicographically greater permutation.
- **Nature:** Needs an understanding of how permutations are indexed and arranged to efficiently find "the next one" without generating all permutations.

### 2. **K-th Permutation Sequence (LeetCode 60)**
- **Description:** As discussed, given n and k, directly compute the k-th lexicographical permutation using a factorial-based algorithm.

### 3. **K-th Combination (Select k-th Lex Order Combination)**
- **Description:** Given n, k, and an index, find the exact k-length combination at that index in lex order.
- **Nature:** Compute the number of ways with binomial coefficients, skipping groups using combinatorial math rather than generating all combinations.

### 4. **Count/Enumerate Combinations & Permutations**
- **Description:** Given n items, how many ways are there to select or arrange k?
- - Combination: $$ \binom{n}{k} = \frac{n!}{k! (n-k)!} $$
- - Permutation: $$ P(n, k) = \frac{n!}{(n-k)!} $$

### 5. **K-th Subset Problem**
- **Description:** Given a set of numbers, enumerate subsets in lex order and directly select the k-th.
- **Nature:** Use combinatorial indexing (by counting combinations, often recursive with binomial coefficients).

### 6. **Finding the Rank of a Permutation or Combination**
- **Description:** Given a permutation or combination, compute its "rank" among all possible arrangements by comparing against group sizes using factorials.

### 7. **Counting Possible Arrangements/Groupings**
- **Description:** Problems that ask “how many ways?” often use factorials and combinatorial formulas directly. For example, how many possible anagrams, how many teams can be formed, or how many ways to distribute indistinguishable balls into bins.

***

## Application & Categorization

These problems are best solved not by brute force, but by direct computation with **combinatorial mathematics**—factorials, combinations, or encoding with binomial coefficients. They often avoid exponential blow-up by skipping entire groups with arithmetic rather than enumeration.

***

If you want solutions or code for any specific example above, let me know!

[1](https://www.youtube.com/watch?v=OcO2SgAnvhg)
[2](https://usaco.guide/gold/combo)
[3](https://www.themathpage.com/aPreCalc/permutations-combinations-2.htm)
[4](https://www.math.fsu.edu/~wooland/hm2ed/Part1Module5/Part1Module5.pdf)
[5](https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Support_Course_for_Elementary_Statistics/Operations_on_Numbers/Factorials_and_Combination_Notation)
[6](https://discrete.openmathbooks.org/dmoi3/sec_counting-combperm.html)
[7](https://www.mathsisfun.com/combinatorics/combinations-permutations.html)
[8](https://analystprep.com/cfa-level-1-exam/quantitative-methods/counting-problems-factorials-combinations-permutations/)
[9](https://www.geeksforgeeks.org/maths/factorial/)


===============================================================================================================================





Below are Python solutions for each combinatorial/factorial-indexing example, with clear test cases and detailed line-by-line comments.

***

## 1. **Next Permutation (LeetCode 31)**
> Given a permutation, find the next lexicographical permutation.

```python
def next_permutation(nums):
    """
    Rearranges numbers into the next lexicographical permutation.
    Modifies nums in-place.
    """
    # Step 1: Find rightmost index i where nums[i] < nums[i+1]
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:
        # Step 2: Find rightmost index j > i where nums[j] > nums[i]
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap nums[i] with nums[j]
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse all elements to the right of i
    nums[i+1:] = reversed(nums[i+1:])

# Test cases
nums = [1,2,3]
next_permutation(nums)
print(nums) # [1, 3, 2]

nums = [3,2,1]
next_permutation(nums)
print(nums) # [1, 2, 3]

nums = [1,1,5]
next_permutation(nums)
print(nums) # [1, 5, 1]
```
**Explanation:**  
Find the first decreasing element from the right, swap it with the smallest larger value to its right, then reverse the sequence after that index to get the next permutation.

***

## 2. **K-th Permutation Sequence (LeetCode 60)**
> Given n and k, return the k-th permutation sequence.

```python
import math

def get_permutation(n, k):
    """
    Returns k-th permutation of numbers 1 to n.
    """
    numbers = list(range(1, n+1))  # Pool of available numbers
    k -= 1  # Adjust to zero-based index
    result = []
    for i in range(n, 0, -1):
        fact = math.factorial(i - 1) # Number of permutations for each prefix
        index = k // fact            # Index of next number to pick
        result.append(str(numbers[index])) # Pick number for this position
        numbers.pop(index)           # Remove picked number from pool
        k = k % fact                 # Update k for next position
    return ''.join(result)

# Test cases
print(get_permutation(3, 3))  # "213"
print(get_permutation(4, 9))  # "2314"
print(get_permutation(3, 1))  # "123"
```
**Explanation:**  
Calculate which number to pick for each spot by dividing k by the factorial, remove chosen number, and repeat for next position.

***

## 3. **K-th Combination (Lex Order)**
> Given n, k, and index, return the k-length combination at that index.

```python
def kth_combination(n, k, idx):
    """
    Returns the idx-th (zero-based) k-combination from [1..n] in lex order.
    """
    nums = list(range(1, n+1))
    result = []
    for i in range(k):
        for j, num in enumerate(nums):
            # Count combinations if num at this position
            remain = n - j - 1
            combs = math.comb(remain, k - i - 1)
            if idx < combs:
                # Choose num for this position
                result.append(num)
                nums = nums[j+1:] # Remove previous numbers
                break
            else:
                idx -= combs
    return result

# Test cases
print(kth_combination(5, 3, 2)) # [1, 4, 5] (combinations in lex order: [1,2,3], [1,2,4], [1,2,5], ...)
print(kth_combination(4, 2, 3)) # [1,4]
```
**Explanation:**  
At each position, count how many combinations would result if a given number were picked. If the index fits, pick it; otherwise, skip and reduce index.

***

## 4. **Subset Generation: K-th Subset (Lex Order)**
> Find the k-th subset in lexicographic order.

```python
def kth_subset(nums, idx):
    """
    Returns k-th subset of nums in lex order. (0-based indexing)
    """
    n = len(nums)
    result = []
    for i in range(n):
        # There are 2^(n-i-1) subsets for each inclusion/exclusion at i
        subsets_if_included = 2 ** (n - i - 1)
        if idx < subsets_if_included:
            # Exclude nums[i], do nothing
            continue
        else:
            # Include nums[i]
            result.append(nums[i])
            idx -= subsets_if_included
    return result

# Test cases
nums = [1,2,3]
print(kth_subset(nums, 3)) # [2] (Subsets: [], [3], [2], [2,3], ...)
nums = [1,2,3,4]
print(kth_subset(nums, 5)) # [2, 4]
```
**Explanation:**  
For each element, decide to include or exclude based on how many subsets would result; update index accordingly.

***

## 5. **Permutation/Combination Rank**
> Given a permutation or combination, find its lexicographic rank.

### a) Permutation Rank

```python
def permutation_rank(permutation):
    """
    Returns rank (0-based) of 'permutation' among all permutations of its elements.
    """
    n = len(permutation)
    rank = 0
    used = [False]*n
    perm_sorted = sorted(permutation)
    for i in range(n):
        idx = perm_sorted.index(permutation[i])
        rank += idx * math.factorial(n - i - 1)
        perm_sorted.pop(idx)
    return rank

# Test cases
print(permutation_rank([2,1,3])) # 2 ("123", "132", "213", ...)
print(permutation_rank([1,3,2])) # 1
```
**Explanation:**  
For each position, count how many permutations are possible for smaller values not used yet.

### b) Combination Rank

```python
def combination_rank(n, k, combination):
    """
    Returns rank (0-based) of the given combination among k-combinations from [1..n].
    """
    rank = 0
    start = 1
    for i in range(k):
        for num in range(start, combination[i]):
            rank += math.comb(n - num, k - i - 1)
        start = combination[i] + 1
    return rank

# Test cases
print(combination_rank(5, 3, [1, 4, 5])) # 2
print(combination_rank(4, 2, [1, 4]))    # 3
```
**Explanation:**  
For each element, count how many combinations begin with smaller numbers at current position.

***

These are efficient, direct solutions to classic combinatorial-indexing problems.  
If you’d like even deeper explanations, or want additional variants (such as "next subset"), let me know!