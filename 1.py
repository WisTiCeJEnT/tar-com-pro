a1 = int(input())
a2 = a1
b = int(input())
ans1 = 0
ans2 = 0
while(a1>=0):
    a1 -= (b/2)*15
    ans1 += 1
while(a2>=0):
    a2 -= (b*9/10)*15
    ans2 += 1
print(ans1)
print(ans2)
