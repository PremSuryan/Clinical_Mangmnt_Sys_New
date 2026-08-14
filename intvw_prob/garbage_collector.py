#Garbage Collector:

"""
A garbage collector is a mechanism that automatically frees memory occupied by objects that are no longer being used by your program.
"""

# Free the memory has two types:
"""
1. Reference Counting
2. Garbage Collector
"""

#1. Reference Counting:

import sys 
a=[1,2,3]
b=a

del a
print(sys.getrefcount(b))

