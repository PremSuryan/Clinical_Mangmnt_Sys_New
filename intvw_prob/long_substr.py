s = "ababcbb"
left = 0
maxi = 0
dupli = set()
for i in range(len(s)):
    while s[i] in dupli:
        dupli.remove(s[left]) 
        left += 1

    dupli.add(s[i])   
    maxi = max(maxi, i-left+1)

print(maxi)