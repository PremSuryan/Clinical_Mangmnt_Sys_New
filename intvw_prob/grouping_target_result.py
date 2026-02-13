l1 = [2,5,4,3,6,1]
target = 7

def group(l1, target):
    res = []
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i] + l1[j] == target:
                res.append((l1[i], l1[j]))
    return res
    # dic = {}
    # for i in l1:
    #     compare = target - i  # 7 - 2 = 5
    #     if compare 
print(group(l1, target))