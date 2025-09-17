
class TrieNode:
    def __init__(self):
        # Each node has a dictionary of children, keys are characters
        self.children = {}
        # Flag to indicate if this node marks the end of a word
        self.is_word = False

class Trie:
    def __init__(self):
        # Root node is an empty TrieNode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            # If character not in children, create a new node
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Mark the end of the word
        node.is_word = True

    def search(self, word: str) -> bool:
        """Return True if word is in trie, False otherwise."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        # Return True if current node marks the end of a word
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        """Return True if any word in the trie starts with the prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        # If traversal was successful, prefix exists in the trie
        return True

# Example usage based on given example:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))    # True
print(trie.search("app"))      # False
print(trie.startsWith("app"))  # True
trie.insert("app")
print(trie.search("app"))      # True


"""
208. Implement Trie (Prefix Tree)
Medium
Topics
premium lock iconCompanies

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.



Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True



Constraints:

    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 104 calls in total will be made to insert, search, and startsWith.


"""