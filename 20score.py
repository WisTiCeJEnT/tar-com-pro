lis = []
his = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(20):
    inp = int(input("Enter score: "))
    if 0 <= inp <= 10:
        his[inp] += 1
        lis.append(inp)
    else:
        print("Score is out of range.")
print("Original list:")
print(lis)
for i in range(11):
    print("{:2} ".format(i)+"*"*his[i])
