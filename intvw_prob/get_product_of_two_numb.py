# Product of two numbers:

number=[1,2,3,4,5]

dic={}
for i in range(len(number)):
    for j in range(len(number)):
        if number[i] != number[j]:
            dic[number[i],number[j]] = number[i]*number[j]

# print(dic)

max_value = max(dic.values())

max_keys = [tuple(sorted(k)) for k, v in dic.items() if v == max_value]

print(max_keys)