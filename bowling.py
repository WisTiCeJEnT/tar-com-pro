Frame = 1
s = 0
while Frame <= 10:
    pin = 10    #pin left
    print("Frame # %d" % Frame)
    d = int(input("Number of pins down: "))
    pin -= d
    if pin > 0:  #strike
        print("Frame # %d" % Frame)
        d = int(input("Number of pins down (0-%d): " % pin))
        pin -= d
    s += 10-pin #Add score
    Frame += 1
print("Total score is %d" % s)
