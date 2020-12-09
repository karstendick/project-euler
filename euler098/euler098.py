with open('p098_words.txt', 'r') as f:
    words = f.read()

words = words.split('","')

sorted_words = sorted(words, key=lambda s: sorted(s))
sorted_words = sorted(sorted_words, key=len, reverse=True)
# for word in words:
#     print('>>' + word)

# print(sorted_words)
anagrams = []
last_word = ''
for word in sorted_words:
    # if len(word) >= 9:
    #     continue
    if len(word) <= 4:
        break
    if sorted(word) == sorted(last_word):
        print(f"{len(word)} | {word} | {sorted(word)}")
        print(f"{len(last_word)} | {last_word} | {sorted(last_word)}")
        anagrams.append((last_word, word))
    last_word = word

print(anagrams)

# nmin, nmax = 10000, 100000
nmin, nmax = 100, 31700
squares = [n*n for n in range(nmin,nmax)]
# squares = [n*n for n in range(nmin,nmax) if n*n < 10**9 and len(set(str(n*n))) == 9]

print(len(squares))

print(sorted(squares, reverse=True))

def get_word_mapping(word, num):
    return dict(zip(word, str(num)))

for left, right in anagrams:
    l = len(left)
    # squares = [n*n for n in range(10**2, 10**5) if n*n < 10**l and len(str(n*n)) == l]
    l_squares = [n for n in squares if len(str(n)) == l]
    for i in l_squares:
        left_word_map = get_word_mapping(left, i)
        for j in l_squares:
            if i == j:
                continue
            right_word_map = get_word_mapping(right, j)
            if left_word_map == right_word_map:
                print(f"{left},{right} | {i},{j}")
