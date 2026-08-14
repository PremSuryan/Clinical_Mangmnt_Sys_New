def sum1(num):
    tol = 0
    for i in num:
        tol+= i

    return tol

num = [1,2,1,0,3,1]
total = sum1(num)
left = 0
for ii in range(len(num)):
    right = total - left - num[ii]

    if left == right:
        print(ii)
        break

    left += num[ii]

else:
    print(-1)
