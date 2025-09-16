def spiralOrder(matrix):
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse down the right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            # Traverse up the left column
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(spiralOrder(matrix1))  # Output: [1,2,3,6,9,8,7,4,5]

matrix2 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print(spiralOrder(matrix2))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]


"""
54. Spiral Matrix
Medium
Topics
premium lock iconCompanies
Hint

Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]



Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100


"""

"""
To return all elements of a matrix in **spiral order**, you can simulate the traversal by maintaining boundaries for rows and columns and shrinking those boundaries as you complete each layer of the spiral.

***

## Approach

- Use four pointers: `top`, `bottom`, `left`, `right` to mark the boundaries.
- Traverse:
  - From left to right across the top row.
  - From top to bottom down the right column.
  - From right to left across the bottom row.
  - From bottom to top up the left column.
- After each traversal, adjust the pointers inward.
- Continue until all elements are visited.

***

## Python Code

```python
def spiralOrder(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse down the right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            # Traverse up the left column
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
```

***

## Example Usage

```python
matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(spiralOrder(matrix1))  # Output: [1,2,3,6,9,8,7,4,5]

matrix2 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print(spiralOrder(matrix2))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

***

## Explanation

- The four boundary pointers keep track of rows and columns not yet traversed.
- Each traversal loop visits one side of the rectangle.
- After completing a side, the boundary shrinks inward.
- The loop continues until boundaries cross (all elements visited).

***

## Complexity

- Time: $$O(m \times n)$$, every element visited exactly once.
- Space: $$O(m \times n)$$ for the output list.

***

**Summary:**  
Using boundary pointers and careful traversal, the matrix can be scanned in spiral order efficiently and cleanly with this standard approach.[1][2]

[1](https://neetcode.io/problems/clone-graph)
[2](https://algo.monster/liteproblems/133)

"""