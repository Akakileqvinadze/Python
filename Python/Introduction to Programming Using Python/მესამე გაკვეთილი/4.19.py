a = int(input("შეიყვანეთ a :"))
b = int(input("შეიყვანეთ b :"))
c = int(input("შეიყვანეთ c :"))
answer = a + b + c
if a + b > c and a + c > b and b + c > a:
    print(f"The perimeter is {answer}:" )
else:
    print("The input is invalid")
