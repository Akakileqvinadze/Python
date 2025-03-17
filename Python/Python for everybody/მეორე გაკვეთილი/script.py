# Diskriminantis gamotvla
# vipovoT diskriminanti x1 da x2.

print("ax^2 +bx +c =0")
print("x=(-b +-(b**2-4ac)**1/2)/2a")
print("თუ (b**2 - 4ac)> 0 მაშინ გვაქვს 2 ამონახსნი x1 ,x2 ."
      "ეს რიცხვებია b=32,a=1,c=2")

print("ეს რიცხვებია")
x1=(-32 +(32**2-4*1*2)**1/2)/2*1
print(x1)
x2=(-32 -(32**2-4*1*2)**1/2)/2*1
print(x2)


# Exercise 2: Write a program that uses input to prompt a user for their
# name and then welcomes them.

input = input("Enter your name:")
print(f"Hellow {input}")

# Exercise 3: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.

a = float(input("Enter Hours:"))
b = float(input("Enter Rate:"))
print(a * b)

# Exercise 4: Assume that we execute the following assignment state-
# ments:

width = 17
height = 12.0

print(width // 2)
print(float(width) / 2.0)
print(height / float(3))
print(1 + 2 * 5)

# Exercise 5: Write a program which prompts the user for a Celsius tem-
# perature, convert the temperature to Fahrenheit, and print out the
# converted temperature.

a = input("sheiyvanet celsiusi: ")
b = float(a) * (9 / 5) + float(32)
print(f"farengeiti arisw:  {b}")


