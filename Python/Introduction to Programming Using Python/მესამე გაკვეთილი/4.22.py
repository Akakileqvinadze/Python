x = int(input("Enter a point with  coordinates x : "))
y = int(input("Enter a point with  coordinates y : "))
answer = int((x ** 2 + y ** 2) ** (1/2))
if answer <= 10:
    print(f"Point {x},{y} is in the circle")
elif answer > 10:
    print(f"Point {x},{y} is not in the circle")
