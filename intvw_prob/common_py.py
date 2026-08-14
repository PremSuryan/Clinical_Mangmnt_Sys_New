# Map , Reduce, Filter and Custom iterator: iterator and Generator

#1. Iterator:
"""
Iterator is a object that gives you only one item at a time instead of giving everything.
number=[1,2,3,4,5] 
number[0],number[1]---> instead of storing everything in memory,
we use num=iter(number)
print(next(num)) ---> it takes less in memory
"""

# number=[1,2,3,4,5] 
# num=iter(number)
# print(next(num))
# print(next(num))
"""
next(num) instead of 
for i in num:
    print(next(i))
"""
# it=[1,22,3,4]
# it_num=iter(it)

# while True:
#     try:
#         print(next(it_num))
#     except StopIteration:
#         break        



#2. Custom Iterator:

# class Custom:
#     def __init__(self,max):
#         self.current=1
#         self.max=max

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current<=self.max:
#             value=self.current
#             self.current+=1
#             return value
#         else:
#             raise StopIteration
        

# obj=Custom(5)
# for i in obj:
#     print(i)

#3. Generators:
"""
A generator is an easier way to create an iterator.
Instead of writing __iter__() python generator gives us yeild
"""
# def gen():
#     yield 1
#     yield 2

# num = gen()
# print(next(num))
# print(next(num))
# print(next(num))

# numbers = (x*x for x in range(5))

# print(next(numbers))
# print(next(numbers))

# 4. Map:
"""
Map applies to function to every element

Syntax:
map(function, iterable not iterator)
"""
# num=[1,2,3,4]

# result = map(lambda x:x*x , num)
# print(list(result))

# 5. Filter():
"""
Filter() removes unwanted data 
Syntax:
filter(function, iterable)
"""

# num=[1,2,3,4,5,6]

# res=filter(lambda x:x%2==0, num)
# print(list(res))

# salary = [25000,50000,70000,90000]

# high = filter(lambda x:x>50000,salary)

# print(list(high))


#6. Reduce:
"""
Reduce converts many values into one values.
Syntax:
reduce(function, iterable)
"""

from functools import reduce

num = [1,2,3,4]

res=reduce(lambda x,y:x+y , num)
print(res)

"""
How reduce works for the num = [1,2,3,4]
List

1 2 3 4

Step 1

1+2=3

Step 2

3+3=6

Step 3

6+4=10
"""