lis = []
lis.append(list(map(int,input().split())))
lis.append(list(map(int,input().split())))
summ = lis[0][0] + lis[0][1] + lis[1][0] + lis[1][1]
ans = summ
for i in range(2,len(lis[0])):
    summ = summ -lis[0][i-2] -lis[1][i-2]
    summ = summ +lis[0][i] +lis[1][i]
    ans = max(ans,summ)
print(ans)
