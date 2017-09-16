count = 0
a = 0
high = 0
while a != -1:
    a = int(input())
    if a > high:
        high = a
        count = count + 1
    else : 
        pass
print("%d" % count)
