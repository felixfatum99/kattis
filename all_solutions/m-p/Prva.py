a, b = map(int, input().split())


shortest_word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"


def check_shortest(word):
    global length_of_word, shortest_word 
    arr = word.split("#")
    for words in arr:
        if len(words) > 1:
            shortest = min(len(words), len(shortest_word))
            for i in range(shortest):
                if ord(words[i]) < ord(shortest_word[i]):
                    shortest_word = words
                    break
                elif ord(words[i]) > ord(shortest_word[i]):
                    break
                elif i == shortest-1:
                    if len(words) == shortest:
                        shortest_word = words

w = ["" for i in range(b)]
for i in range(a):
    line = input()
    check_shortest(line)
    for i in range(len(line)):
        w[i]+=line[i]

for i in range(len(w)):
    line = w[i]
    check_shortest(line)

print(shortest_word)
    
