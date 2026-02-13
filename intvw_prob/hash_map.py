
def anagram(inp):
    dic = {}
    res = []
    
    for i in inp:
        sorting = "".join(sorted(i))
        if sorting not in dic:
            dic[sorting] = [i]
            
        else:
            dic[sorting].append(i)

    # print(dic)    
    # print("res", res.append(dic.values()))    
    for ii in dic.values():
        res.append(ii)
    return res

inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagram(inp))