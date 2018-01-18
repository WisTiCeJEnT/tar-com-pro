a1,b1,c1 = map(float,input().split())
a2,b2,c2 = map(float,input().split())
#try:
if a1 != 0:
    y = ((a2/a1)*c1 - c2) / (b2 - (a2/a1)*b1)
    x = -(b1*y + c1) / a1
    print(x,y)
#except ZeroDivisionError:
else:
    if b1 != 0 and a2 != 0:
        y = -c1 / b1
        x = (b2*c1/b1 - c2) / a2
        print(x,y)
    else:
        print("error")
