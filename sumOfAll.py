lis = []
inp = int(input("Enter a number (0 to end): "))
while inp!=0:
    lis.append(inp)
    inp = int(input("Enter a number (0 to end): "))
print("Original list:")
print(lis)
print("Accumulative Sum:")
ans = 0
for i in lis:
    ans += i
    print(ans)
