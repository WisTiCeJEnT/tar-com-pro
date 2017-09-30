i = 0
n = int(input())
while i<n:
    j = 0
    while j < n-i:
        print("*",end="")
        j += 1  
    print()
    i += 1
