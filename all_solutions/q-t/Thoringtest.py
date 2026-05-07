n = int(input())
words = []
for _ in range(n):
    word = input().lower()
    words.append(word)

sentence = [word.lower() for word in input().split()]
works = True

for w in sentence:
    if w not in words:
        works = False

if works:
    print("Hi, how do I look today?")
else:
    print("Thore has left the chat")