scores = input("Enter scores: ").split()
scores = [int(i) for i in scores]
grade = max(scores)
for f in scores:
  if f>=grade-10:
    print(f"Student 0 score is {f} and grade is A")
  elif f>=grade-20:
    print(f"Student 0 score is {f} and grade is B")
  elif f>=grade-30:
    print(f"Student 0 score is {f} and grade is C")
  elif f>=grade-40:
    print(f"Student 0 score is {f} and grade is D")
  else:
    print("The grade is F otherwise.")
