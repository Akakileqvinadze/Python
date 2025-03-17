# Introduction to Programming Using Python
# 2.1

a = input("Enter a degree in Celsius: ")
b = (9 / 5) * float(a) + float(32)
print(f"{a} Celsius is {b} Fahrenheit")


# 2.2

radius = input("Enter the radius of a cylinder: ")
length = input("Enter the length of a cylinder: ")

area = float(radius) * float(radius) * 3.14
volume = float(area) * float(length)
print(f"The area is {area}")
print(f"The volume is {volume}")


# 2.3

feet = float(input("Enter a value for feet: "))
answer = feet * 0.305
print(f"{feet} feet is {answer} meters")



# 2.4

pounds = float(input("Enter a value in pounds: "))
kilograms = pounds * 0.454
print(f"{pounds} pounds is {kilograms} kilograms")

# 2.5

subtotal = float(input("Enter the subtotal :"))
gratuity = float(input("Enter the  gratuity rate:"))
answer = subtotal * gratuity / 100
total = gratuity + answer
print(f"The gratuity is {answer} and the total is {total}")




# 2.6

number = input("Enter a number between 0 and 1000: ")
answer = int(number[0]) + int(number[1]) + int(number[2])
print(f"The sum of the digits is {answer}")


# 2.7

number = int(input("Enter the number of minutes: "))
hour = number / 60
day = hour / 24
yer = day / 365
print(f"{number} minutes is approximately {yer} years")