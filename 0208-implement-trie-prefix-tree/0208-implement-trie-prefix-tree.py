class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # Create a new node if the character doesn't exist
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of a word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            # If character doesn't exist, return False
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word  # Only return True if full word ends here

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            # If character doesn't exist, prefix not found
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # Prefix exists
