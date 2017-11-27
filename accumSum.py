lis = []
inp = int(input("Enter a number (0 to end): "))
while inp!=0:
    if 1<=inp<=999:
        lis.append(inp)
    else:
        print("Number is out of range.")
    inp = int(input("Enter a number (0 to end): "))
print("Original list:")
print(lis)
print("Accumulative Sum:")
ans = 0
for i in lis:
    ans += i
    print(ans)
