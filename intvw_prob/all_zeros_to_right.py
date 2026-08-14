"""
Move all zero to right!
"""


num=[1,0,2,0,5,0]

# non_zero=[]
# zeros=[]

# for i in num:
#     if i ==0:
#         zeros.append(i)

#     else:
#         non_zero.append(i)
# non_zero.extend(zeros)   #-------> [1, 2, 5, 0, 0, 0]
# # zeros.extend(non_zero)  --------> [0, 0, 0, 1, 2, 5]

# print(non_zero)
# print(zeros)

left=0
right=0

while right < len(num):
    if num[right] != 0:
        num[left] ,num[right] = num[right], num[left]
        left += 1

    right += 1

print(num)