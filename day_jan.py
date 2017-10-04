day = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
x = int(input())
y = int(input())
if 1 < y < 31:
    y -= x
    y = y%7
    print(day[y])
else:
    print("ERROR")
