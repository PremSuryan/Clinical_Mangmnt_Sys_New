"""
Find Duplicate number
[1,2,3,4,5,2,1,5,4]
"""

inp=[1,2,3,4,5,2,1,5,4]

dicti={}

for i in range(len(inp)):
    j=inp[i]
    if j in dicti:
        dicti[j]+=1

    else:
        dicti[j]=1


res=[]
for k,v in dicti.items():
    if v >1:
        res.append(k)
    else:

        continue

print(res)
