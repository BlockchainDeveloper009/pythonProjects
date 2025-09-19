
def exist(board, word):
    ROWS, COLS = len(board), len(board[0])

    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS
            or board[r][c] != word[idx]):
            return False

        # Mark visited
        temp = board[r][c]
        board[r][c] = '#'

        # Explore neighbors
        found = (dfs(r + 1, c, idx + 1) or
                 dfs(r - 1, c, idx + 1) or
                 dfs(r, c + 1, idx + 1) or
                 dfs(r, c - 1, idx + 1))

        # Backtrack
        board[r][c] = temp

        return found

    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    return False



board1 = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
print(exist(board1, "ABCCED"))  # True
print(exist(board1, "SEE"))     # True
print(exist(board1, "ABCB"))    # False



"""
79. Word Search
Medium
Topics
premium lock iconCompanies

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false



Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.



Follow up: Could you use search pruning to make your solution faster with a larger board?

"""

"""
The **Word Search** problem can be solved using **backtracking (DFS)** to explore possible paths on the grid that form the given word.

***

## Approach

1. Loop over all cells.
2. For each cell, start a DFS if the first letter matches the word’s first character.
3. In DFS:
   - Check if current cell matches current character in word.
   - If yes, recurse on its 4 neighbors (up, down, left, right) for the next character.
   - Mark the current cell as visited to avoid reuse in the same path.
   - Backtrack (unmark cell) if path doesn’t lead to a solution.
4. If full word matched, return True.

***

## Python Code

```python
def exist(board, word):
    ROWS, COLS = len(board), len(board[0])

    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS 
            or board[r][c] != word[idx]):
            return False

        # Mark visited
        temp = board[r][c]
        board[r][c] = '#'

        # Explore neighbors
        found = (dfs(r + 1, c, idx + 1) or
                 dfs(r - 1, c, idx + 1) or
                 dfs(r, c + 1, idx + 1) or
                 dfs(r, c - 1, idx + 1))

        # Backtrack
        board[r][c] = temp

        return found

    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    return False
```

***

## Example Usage

```python
board1 = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
print(exist(board1, "ABCCED"))  # True
print(exist(board1, "SEE"))     # True
print(exist(board1, "ABCB"))    # False
```

***

## Explanation

- DFS explores all paths from matching start cells.
- Marking cells as visited avoids revisits on same path.
- Backtracking restores state for other attempts.

***

## Optimization (Search Pruning)

- Count characters in board and word to quickly return False if word contains chars missing or insufficient in board.
- Start DFS from the least frequent letter positions for faster pruning.
- Early exit once word is matched.

***

## Complexity

- Time: Worst case $$O(m \times n \times 4^L)$$, where L is word length.
- Space: $$O(L)$$ for recursion stack.

***

**Summary:**  
Backtracking with pruning and careful visited marking solves Word Search efficiently on small boards by exploring all possible paths to build the target word.[1][2]

[1](https://neetcode.io/problems/clone-graph)
[2](https://algo.monster/liteproblems/133)
"""