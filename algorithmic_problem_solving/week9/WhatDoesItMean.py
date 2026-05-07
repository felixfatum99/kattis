class Trie:
    class Node:
        def __init__(self, character=None):
            self.alphabet = [None] * 26
            self.isWord = False
            self.character = character
            self.children = 0
            self.meanings = 0
    
    def __init__(self):
        self.root = self.Node()
    
    def find_index(self, letter):
        return ord(letter) - ord('a')
    
    def insert_word(self, word, meanings):
        current_node = self.root 

        for letter in word:
            index = self.find_index(letter)

            if current_node.alphabet[index] is None:
                new_node = self.Node(letter)
                current_node.alphabet[index] = new_node
                
            current_node = current_node.alphabet[index]
            current_node.children += 1

        current_node.isWord = True
        current_node.meanings = meanings


n, name = input().split()
n = int(n)

T = Trie()

for _ in range(n):
    word, count = input().split()
    count = int(count)
    T.insert_word(word, count)

m = len(name)

dp = [0] * (m + 1)
dp[m] = 1

for i in range(m - 1, -1, -1):
    current_node = T.root

    for j in range(i, m):
        index = T.find_index(name[j])

        if current_node.alphabet[index] is None:
            break

        current_node = current_node.alphabet[index]

        if current_node.isWord:
            dp[i] = (dp[i] + current_node.meanings * dp[j + 1]) % (10**9 + 7)

print(dp[0])