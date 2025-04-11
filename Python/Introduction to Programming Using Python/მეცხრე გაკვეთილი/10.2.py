lst = [10, 3, 5, 4, 6, 7, 3, 2, 3, 4]
print(lst)
f=0
i = 1
while len(lst)-f>0:
    answer=lst[len(lst)-i]
    i=i+1
    f=f+1
    print(answer,end=",")
