import sys

all_words = set()
for line in sys.stdin:
    words = line.split()
    for word in words:
        all_words.add(word)
all_words = list(all_words)
s =set() 
for i in range(len(all_words)):
    for j in range(len(all_words)):
        if all_words[i] != all_words[j]:
            s.add(all_words[i]+all_words[j])

for l in sorted(list(s)):
    print(l)