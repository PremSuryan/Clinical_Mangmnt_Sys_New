# max sequence number:

l=[1,1,1,0,1,1,1,1]


max_count=1
count=1

for i in range(1,len(l)):
    if l[i]==l[i-1]:
        count+=1
    else:
        count=1
        max_count=max(max_count,count)
        
print(max(max_count,count))

