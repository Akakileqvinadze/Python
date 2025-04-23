nums = input("Sheiyvanet sityva :").split()
a = [int(i) for i in nums]
a.sort()
print(a)
b = []
for z in range(len(a)//2):
    b.append(a[len(a) - z -1])
    b.append(a[z])
if len(a)%2==1:
    b.append(a[len(a)//2])
print(b)








        
