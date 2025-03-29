balance = 1000
print(f"your balance :{balance}")
print("1) withdraw")
print("2) deposit")
print("3) check")
operation = int(input("enter operation you want to perform: "))
if operation == 3:
    print(f"new balance: {balance}")
elif operation == 2:
    answer =int(input("enter amount you want to deposit: "))
    answer1 = balance + answer
    print(f"new balance: {answer1}")
elif operation == 1:
    answer3 = int(input("enter amount you want to deposit: "))
    answer4 = balance - answer3
    if answer4 < 0:
        print("insufficient found")
    else:
        print(f"new balance: {answer4}")

