def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

    # Use first row and col as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero rows based on markers
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0

    # Zero columns based on markers
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0

    # Zero first row if needed
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0

    # Zero first column if needed
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0



matrix1 = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
setZeroes(matrix1)
print(matrix1)
# Output:
# [[1,0,1],[0,0,0],[1,0,1]]

matrix2 = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]
setZeroes(matrix2)
print(matrix2)
# Output:
# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


"""
73. Set Matrix Zeroes
Medium
Topics
premium lock iconCompanies
Hint

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

 

Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1

"""

"""
To solve the problem of setting matrix rows and columns to zero **in-place** with **constant extra space**, we can use the first row and the first column of the matrix itself as markers.

***

## Approach

1. **Use first row and first column as markers:**
   - Scan the matrix.
   - If `matrix[i][j] == 0`, mark the corresponding row and column for zeroing by setting `matrix[i] = 0` and `matrix[j] = 0`.

2. **Keep track if first row and first column originally contained any zeros:**
   - Use two boolean variables to store whether the first row or first column need to be zeroed later.

3. **Perform zeroing based on markers:**
   - Set entire row to zero if `matrix[i] == 0`.
   - Set entire column to zero if `matrix[j] == 0`.

4. **Finally, zero out the first row and first column as necessary.**

***

## Python Code

```python
def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

    # Use first row and col as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero rows based on markers
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0

    # Zero columns based on markers
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0

    # Zero first row if needed
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0

    # Zero first column if needed
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0
```

***

## Example Usage

```python
matrix1 = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
setZeroes(matrix1)
print(matrix1)
# Output:
# [[1,0,1],[0,0,0],[1,0,1]]

matrix2 = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]
setZeroes(matrix2)
print(matrix2)
# Output:
# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

***

## Explanation

- The first row and column are used to store information about which row or column should be zeroed, saving extra space.
- Careful handling is done for the first row and column themselves because we use them as markers.
- This approach uses only **constant extra space**.

***

## Complexity

- Time: $$O(m \times n)$$, where $$m, n$$ are matrix dimensions.
- Space: $$O(1)$$, in-place without additional data structures.

***

**Summary:**
By using the matrix’s first row and column as marker storage, this solution zeroes out rows and columns in-place efficiently with constant space overhead, meeting the problem’s constraints and follow-up requirements.

[1](https://en.wikipedia.org/wiki/In-place_algorithm)
"""