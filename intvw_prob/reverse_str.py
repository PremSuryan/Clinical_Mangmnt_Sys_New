# name = "Prem Suryan"
# out = "nayruS merP"

# out1 = []
# res = name.split(" ")[::-1]
# for i in res:
#     out1.append(i[::-1])
# print(" ".join(out1))

# name = "prem"
# print(name[::-1])

# lst = [[1, 2, 3], [4, 5]]

# print(lst[::-1])

"""
Reverse string

Without slicing.
"""
name="Prem Suryan"

reverse=""
for n in name:
    reverse=n+reverse

print(reverse)


name = "Prem Suryan"

i = len(name) - 1

while i >= 0:
    print(name[i], end="")
    i -= 1


name = "Prem Suryan"

i = len(name) - 1
reverse=""
while i >= 0:
    reverse+=name[i]
    i -= 1

print(reverse)