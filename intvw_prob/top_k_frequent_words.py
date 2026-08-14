"""
Top K frequent words:
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
"""
words = ["i", "love", "leetcode", "i", "love", "coding"]

word_dict={}

for word in words:
    if word not in word_dict:
        word_dict[word]=0

    word_dict[word]+=1

print(word_dict)

freq_word=[]
for i,v in word_dict.items():
    if v >=2:
        freq_word.append(i)

print(freq_word)
