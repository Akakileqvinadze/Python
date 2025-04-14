lst = [1,2,3,2,1,6,3,4,5,2]
answer = []
for i in lst:
 if i not in answer:
    answer.append(i)
print(answer)