class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
# --------------------------------------------------------------------------

class Trie:
    def __init__(self):
        self.root = TrieNode()

# --------------------------------------------------------------------------

    def insert(self, word):
        temp = self.root
        for i in word:
            if i not in temp.children:
                temp.children[i] = TrieNode()
            temp = temp.children[i]
        temp.end_of_word = True

# --------------------------------------------------------------------------

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end_of_word

# --------------------------------------------------------------------------

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
    
# --------------------------------------------------------------------------

    def delete(self, word):
        def _delete(node, word, index):
            if index == len(word):
                if node.end_of_word:
                    node.end_of_word = False
                    return len(node.children) == 0
                return False
            
            char = word[index]
            if char in node.children:
                child_node = node.children[char]
                should_delete_child = _delete(child_node, word, index + 1)
                if should_delete_child:
                    del node.children[char]
                    return len(node.children) == 0
            return False

        _delete(self.root, word, 0)

# --------------------------------------------------------------------------

trie = Trie()

# Insert some words into the Trie
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")
trie.insert("pear")
# 
# Search for some words in the Trie
print(trie.search("apple"))  
print(trie.search("banana")) 
print(trie.search("grape"))  
# 
# Check if any words start with a prefix
print(trie.starts_with("app")) 
print(trie.starts_with("ban")) 
print(trie.starts_with("gra")) 

# Search for the deleted word
print(trie.delete("banana"))  

print("-------------------------------")

# Check if any words start with a prefix
print(trie.starts_with("ban"))  
print(trie.starts_with("ora")) 