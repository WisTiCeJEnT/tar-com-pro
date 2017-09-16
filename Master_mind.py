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
     print('%d position correct, %d digits correct' % (x,o))
    if x == 4:
     print('Congratulations, you just mastered my mind!!')
