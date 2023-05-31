class Trie:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

# --------------------------------------------------------------------------------
    def insert(self, word):
        temp = self
        for i in word:
            if i not in temp.children:
                temp.children[i] = Trie()
                temp = temp.children[i]
        temp.is_end_of_word = True
# --------------------------------------------------------------------------------

    def search(self, word):
        current = self
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word
# --------------------------------------------------------------------------------

    def delete(self, word):
        def _delete_helper(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            should_delete_child = _delete_helper(node.children[char], word, index + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0

            return False
# --------------------------------------------------------------------------------


# Example usage
trie = Trie()

# Insertion
trie.insert("apple")
trie.insert("app")
trie.insert("banana")

# Searching
print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("banana")) # Output: True
print(trie.search("grape"))  # Output: False
