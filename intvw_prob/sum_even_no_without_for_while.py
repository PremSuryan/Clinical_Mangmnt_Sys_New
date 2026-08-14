#sum_even_no_without_for_while.

numb=[1,4,6,1,3,7,2]

# even_list=[ i for i in numb if i%2==0]

from functools import reduce

# print(reduce(lambda x,y :x+y, even_list)

# i=0
# count=0
# while i<len(numb):
#     if numb[i]%2==0:
#         count+=numb[i]
#     else:
#         continue
#     i+=1
# print(count)


#without for or while loop:
# print(sum(filter(lambda x:x%2==0, numb))) 

print(reduce(lambda a,b: a+b if b%2==0 else a, numb,0))