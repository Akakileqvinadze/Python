answer = input("Enter integers between 1 and 100: ")
answer1 = [int(i)for i in answer.split()]
z=0
f=0
i = 1
while len(answer1)-f>0:
    print(f"{answer1[z]} occures  {answer1.count(answer1[z])}")
    f=f+1
    z=z+1