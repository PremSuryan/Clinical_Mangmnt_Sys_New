"""
Merge intervals

[1,3]
[2,5]
[8,10]

Output

[1,5]
[8,10]

Answer:
What does an interval mean?

An interval

[1,3]

means

1 -------- 3

Another interval

[2,5]

means

    2 ----------- 5

Draw them together:

1 -------- 3
    2 ----------- 5

They overlap.

So they become

1 ---------------- 5

which is

[1,5]

NOTE:
this will not overlap
1 -------- 2
    3 ----------- 5

steps to follow:
Another example
[1,2]
[4,6]

Picture

1---2

        4----6

They don't touch.

Keep them separate.

Output

[[1,2],[4,6]]    

step1:
sort the input
suppose the input is [
    [8,10],
    [1,3],
    [2,5]
]
Sorting gives

[
    [1,3],
    [2,5],
    [8,10]
]
"""

intervals = [[1,3],[2,5],[8,10]]

intervals.sort()

merged=[]

for interval in intervals:
    if not merged:
        merged.append(interval)
    elif interval[0] <= merged[-1][1]:
        merged[-1][1]=max(merged[-1][1],interval[1])

    else:
        merged.append(interval)

print(merged)