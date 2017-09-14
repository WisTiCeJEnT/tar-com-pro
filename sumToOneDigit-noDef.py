inp = int(input())
while inp > 9:
    tmp = 0
    while inp>0:
        tmp += inp%10
        inp = inp//10
    inp = tmp
print(inp)
