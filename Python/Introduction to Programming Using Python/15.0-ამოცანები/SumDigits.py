
def sumDigits(n):
    ricxvistringshi = str(n)
    List = []
    for i in ricxvistringshi:
        answer =int(i)
        List.append(answer)
    Aswer = sum(List)
    return Aswer

print(sumDigits(1233333))