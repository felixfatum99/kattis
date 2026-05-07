class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            curr.count += 1

        curr.isLeaf = True

    def search(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isLeaf

    def get_prefix_count(self, prefix):
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return 0
            curr = curr.children[index]
        return curr.count

n = int(input())
trie = Trie()

for _ in range(n):
    w = input()
    print(trie.get_prefix_count(w))
    trie.insert(w)