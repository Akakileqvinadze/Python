number = int(input("შეიყვანეთ ციფრი"))
number1 = int(input("შეიყვანეთ ციფრი"))
number2 = int(input("შეიყვანეთ ციფრი"))

answer = number,number1,number2
middle = number+number1+number2-(min(answer)+max(answer))
print(f"ციფრები თანმიმდევრობითი {min(answer)},{middle},{max(answer)}")