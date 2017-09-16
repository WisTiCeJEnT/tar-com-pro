def conv(n):
    n = str(n)
    dic = {'1':"one" , '2':"two" , 
        '3':"three" , '4':"four" , 
        '5':"five" , '6':"six" , 
        '7':"seven" , '8':"eight" , 
        '9':"nine" , '0':"no"}
    return dic[n]
def firstChar(s):
    s = s[0].upper() + s[1::len(s)]
    return s
ans = str(input("Enter a target (4-digit integer): "))
ans = '0'*(4-len(ans)) + ans        #Add 0 if ans < 1000
g = -1
if (g != ans):
    x = 0
    o = 0
    g = input("Enter your guess (4-digit integer): ")
    for i in range(0,min(len(ans),len(g))):
        if g[i] == ans[i]:
            x += 1
        elif g[i] in ans:
            o += 1
    if x != 4:
     print('%s position correct, %s digits correct' % (firstChar(conv(x)),conv(o)))
    if x == 4:
     print('Congratulations, you just mastered my mind!!')
