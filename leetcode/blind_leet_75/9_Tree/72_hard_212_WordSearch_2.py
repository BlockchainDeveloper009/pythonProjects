class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store word at end node


class Solution:
    def findWords(self, board, words):
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        ROWS, COLS = len(board), len(board[0])
        result = set()

        def backtrack(r, c, parent):
            letter = board[r][c]
            curr_node = parent.children.get(letter)
            if not curr_node:
                return
            # Check if word ends here
            if curr_node.word:
                result.add(curr_node.word)
                curr_node.word = None  # avoid duplicates

            # Mark visited
            board[r][c] = '#'

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#':
                    backtrack(nr, nc, curr_node)

            # Restore
            board[r][c] = letter

            # Optimization: remove leaf node if no children to prune trie
            if not curr_node.children:
                parent.children.pop(letter)

        for i in range(ROWS):
            for j in range(COLS):
                backtrack(i, j, root)

        return list(result)



board = [
  ["o","a","a","n"],
  ["e","t","a","e"],
  ["i","h","k","r"],
  ["i","f","l","v"]
]
words = ["oath","pea","eat","rain"]
sol = Solution()
print(sol.findWords(board, words))  # Output: ["eat", "oath"]


"""
212. Word Search II
Hard
Topics
premium lock iconCompanies
Hint

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []



Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.


"""


"""
The **Word Search II** problem asks to find all words from a given list that can be formed on the board by moving horizontally or vertically without reusing cells. Due to the large input size and multiple words, an efficient approach uses a **Trie** combined with backtracking.

***

## Approach: Trie + Backtracking

- Build a Trie from the list of words for quick prefix lookup.
- For each cell on the board, perform DFS:
  - Explore neighbors for possible next characters.
  - Use Trie to prune paths that cannot lead to valid words.
- Mark visited cells temporarily.
- Collect words found in a set to avoid duplicates.

***

## Python Code

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store word at end node

class Solution:
    def findWords(self, board, words):
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
        
        ROWS, COLS = len(board), len(board[0])
        result = set()
        
        def backtrack(r, c, parent):
            letter = board[r][c]
            curr_node = parent.children.get(letter)
            if not curr_node:
                return
            # Check if word ends here
            if curr_node.word:
                result.add(curr_node.word)
                curr_node.word = None  # avoid duplicates
            
            # Mark visited
            board[r][c] = '#'
            
            for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#':
                    backtrack(nr, nc, curr_node)
            
            # Restore
            board[r][c] = letter
            
            # Optimization: remove leaf node if no children to prune trie
            if not curr_node.children:
                parent.children.pop(letter)
        
        for i in range(ROWS):
            for j in range(COLS):
                backtrack(i, j, root)
        
        return list(result)
```

***

## Explanation

- Trie enables pruning search paths early if next character doesn't lead to any word.
- Backtracking explores all paths and uses marks to avoid revisiting same cell.
- Words found are stored in `result` with deduplication by clearing `word` in Trie.
- Trie nodes are pruned when their children are exhausted to speed up search.

***

## Example Usage

```python
board = [
  ["o","a","a","n"],
  ["e","t","a","e"],
  ["i","h","k","r"],
  ["i","f","l","v"]
]
words = ["oath","pea","eat","rain"]
sol = Solution()
print(sol.findWords(board, words))  # Output: ["eat", "oath"]
```

***

## Complexity

- Time roughly $$O(M \times 4^{L})$$, where $$M$$ is board cells and $$L$$ max word length.
- Trie and pruning significantly reduce unnecessary search paths.

***

**Summary:**  
Combining Trie for prefixes and DFS backtracking on the board enables efficient word search even with large word lists by pruning invalid paths early.

"""