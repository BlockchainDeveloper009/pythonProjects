class TrieNode:
    def __init__(self):
        self.children = {}  # Mapping from char to TrieNode
        self.is_word = False  # Marks end of a word


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_word
            if word[i] == '.':
                # Try all possible child nodes
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]], i + 1)

        return dfs(self.root, 0)


wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
print(wd.search("pad"))  # False
print(wd.search("bad"))  # True
print(wd.search(".ad"))  # True
print(wd.search("b.."))  # True


"""
211. Design Add and Search Words Data Structure
Medium
Topics
premium lock iconCompanies
Hint

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.



Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True



Constraints:

    1 <= word.length <= 25
    word in addWord consists of lowercase English letters.
    word in search consist of '.' or lowercase English letters.
    There will be at most 2 dots in word for search queries.
    At most 104 calls will be made to addWord and search.


"""

"""
The **WordDictionary** class supports word addition and wildcards search (with `.` matching any letter). The most efficient solution uses a **Trie (prefix tree)** with recursive search for the dot-wildcard cases.

***

## Approach: Trie and Recursive Search

- Store words in a Trie for efficient add and search.
- For `search`, traverse Trie recursively:
  - If a character is a dot (`.`), recursively try all children.
  - If a regular character, follow the matching child.

***

## Python Code

```python
class TrieNode:
    def __init__(self):
        self.children = {}     # Mapping from char to TrieNode
        self.is_word = False   # Marks end of a word

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_word
            if word[i] == '.':
                # Try all possible child nodes
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]], i + 1)
        return dfs(self.root, 0)
```

***

## Explanation

- **addWord:** Inserts each character into the Trie; marks the end node.
- **search:** Uses recursive DFS. On dot, tries all children; on letter, follows the matching path.
- Efficient for up to 10^4 operations and supports two wildcards.

***

## Example Usage

```python
wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
print(wd.search("pad"))  # False
print(wd.search("bad"))  # True
print(wd.search(".ad"))  # True
print(wd.search("b.."))  # True
```

***

## Complexity

- **addWord:** $$O(L)$$, L=word length
- **search:** Worst-case $$O(26^D \cdot L)$$, D=maximum wildcards (2 dots = 676 branches max), L=word length.

***

**Summary:**  
Trie + recursive search allows adding and wildcard-matching efficiently, leveraging Trie structure for quick lookup and dot handling.
"""