#https://open.kattis.com/problems/bing
class Trie:
    class Node:
        def __init__(self, character=None):
            self.alphabet = [None] * 26
            self.isWord = False
            self.character = character
            self.children = 0
    
    def __init__(self):
        self.root = self.Node()
    
    def find_index(self, letter):
        return ord(letter) - ord('a')
    
    def insert_word(self, word):
        current_node = self.root 

        for letter in word:
            index = self.find_index(letter)

            if current_node.alphabet[index] is None:
                new_node = self.Node(letter)
                current_node.alphabet[index] = new_node
                
            current_node = current_node.alphabet[index]
            current_node.children += 1

        current_node.isWord = True
    
    def search_for_word(self, word):
        current_node = self.root

        for letter in word:
            index = self.find_index(letter)
            
            if current_node.alphabet[index] is None:
                return False
            
            current_node = current_node.alphabet[index]

        return current_node.isWord

    def prefix_count(self, word):
        current_node = self.root

        for letter in word:
            index = self.find_index(letter)
            
            if current_node.alphabet[index] is None:
                return 0
            
            current_node = current_node.alphabet[index]

        return current_node.children


N = int(input())
T = Trie()

for _ in range(N):
    word = input()
    print(T.prefix_count(word))
    T.insert_word(word)