# Diskriminantis gamotvla
# vipovoT diskriminanti x1 da x2.
#from script1 import answer

print("ax^2 +bx +c =0")
print("x=(-b +-(b**2-4ac)**1/2)/2a")
print("თუ (b**2 - 4ac)> 0 მაშინ გვაქვს 2 ამონახსნი x1 ,x2 ."
      "ეს რიცხვებია b=32,a=1,c=2")

print("ეს რიცხვებია")
a=float(input("შეიყვანეთ a კოეფიციენტი"))
b=float(input("შეიყვანეთ b კოეფიციენტი"))
c=float(input("შეიყვანეთ c კოეფიციენტი"))

answer = b**2 - 4*a*c
print(f"discriminant:{answer}")
x1=float(-b +(b**2-4*a*c)**(1/2))/(2*a)
print(f"x1 = {x1}")
x2=float(-b -(b**2-4*a*c)**(1/2))/(2*a)
print(f"x2 = {x2}")


