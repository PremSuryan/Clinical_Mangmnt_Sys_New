"""
Print Hello 10 times without using loop:
"""

# One way:
# print("Hello\n" * 10, end=" ")

#Another way:

def number(n):
    if n==0:
        return
    
    print("Hello")
    number(n-1)


number(10)