a = int(input("Enter an integer: "))
if a % 5 ==0 and a%6==0:
    print(f"Is {a} divisible by 5 and 6? true")
else:print(f"Is {a} divisible by 5 and 6? false")
if a % 5==0 or a % 6==0:
    print(f"Is {a} divisible by 5 and 6? true")
else:print(f"Is {a} divisible by 5 and 6? false")
if not(a % 5==0 and  a % 6==0):
    print(f"Is {a} divisible by 5 or 6, but not both? true")
else:print(f"Is {a} divisible by 5 or 6, but not both? false")