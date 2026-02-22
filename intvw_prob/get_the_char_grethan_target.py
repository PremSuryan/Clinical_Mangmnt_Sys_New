arr = ['c','f','g']
target = 'a'
tar_val = ord(target)
print(tar_val)
dic = {}
for i in arr:
    dic[i] = ord(i)
print(dic)

for key,val in dic.items():
    if tar_val < val:
        print(key)
        break
    else:
        continue