import random

a = int(input("scissor (0), rock (1), paper (2): "))
random = abs(random.randint(0, 2))
computer = "null"
me = "null"
answer = "null"

if random == 0:
    computer = "scissor"
elif random == 1:
    computer = "rock"
elif random == 2:
    computer = "paper"

if a == 0:
    me = "scissor"
elif a == 1:
    me = "rock"
elif a == 2:
    me = "paper"

if random == 0 and a == 0:
    answer = "It is a draw"
elif random == 0 and a == 1:
    answer = "you won"
elif random == 0 and a == 2:
    answer = "you loss"
elif random == 1 and a == 0:
    answer = "you loss"
elif random == 1 and a == 1:
    answer = "It is a draw"
elif random == 1 and a == 2:
    answer = "you won"
elif random == 2 and a == 0:
    answer = "you won"
elif random == 2 and a == 1:
    answer = "you loss"
elif random == 2 and a == 2:
    answer = "It is a draw"

print(f"The computer is {computer}. You are {me}. {answer}.")
