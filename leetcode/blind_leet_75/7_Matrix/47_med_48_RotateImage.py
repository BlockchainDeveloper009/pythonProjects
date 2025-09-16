def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix (swap across the diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()


matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rotate(matrix1)
print(matrix1)
# Output:
# [[7,4,1],
#  [8,5,2],
#  [9,6,3]]

matrix2 = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]
rotate(matrix2)
print(matrix2)
# Output:
# [[15,13,2,5],
#  [14,3,4,1],
#  [12,6,8,9],
#  [16,7,10,11]]



"""
48. Rotate Image
Medium
Topics
premium lock iconCompanies

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.



Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]



Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000


"""


"""
To rotate an n x n matrix by 90 degrees clockwise **in-place**, the typical approach is to:

1. **Transpose** the matrix: swap elements across the diagonal.
2. **Reverse** each row.

This method modifies the input matrix directly without extra space beyond a few variables.

***

## Step-by-step

- **Transpose:** Swap matrix[i][j] and matrix[j][i] for all i < j.
- **Reverse rows:** For each row, reverse the entire row.

***

## Python Code

```python
def rotate(matrix):
    n = len(matrix)
    
    # Transpose the matrix (swap across the diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
```

***

## Example Usage

```python
matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rotate(matrix1)
print(matrix1)
# Output:
# [[7,4,1],
#  [8,5,2],
#  [9,6,3]]

matrix2 = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]
rotate(matrix2)
print(matrix2)
# Output:
# [[15,13,2,5],
#  [14,3,4,1],
#  [12,6,8,9],
#  [16,7,10,11]]
```

***

## Explanation

- Transpose reflects the matrix along its diagonal, turning rows into columns.
- Reversing each row completes the 90-degree clockwise rotation.
- Both operations are done **in place**.

***

## Complexity

- Time: $$O(n^2)$$, all elements are visited a constant number of times.
- Space: $$O(1)$$ extra space, done in-place.

***

**Summary:**  
Transpose then reverse rows rotates the matrix in place efficiently and elegantly without allocating extra space, meeting the problem requirements.[1][2]

[1](https://neetcode.io/problems/clone-graph)
[2](https://algo.monster/liteproblems/133)
"""