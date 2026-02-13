# aaabb → a3b2
inp= "aaabb"
dic = {}

for i in inp:
  if i not in dic:
    dic[i] = 1

  else:
    dic[i] += 1

res = ""

for ii, val in dic.items():
  res += f"{ii}{val}"


print(res)