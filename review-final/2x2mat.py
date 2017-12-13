lis = []            #prepare list for 2x2 matrix
lis.append(list(map(int,input().split())))  #add row 0 to mat
lis.append(list(map(int,input().split())))  #add row 1 to mat
summ = lis[0][0] + lis[0][1] + lis[1][0] + lis[1][1] #sum of first 2x2 on the left #!!! It's gonna error here if the input is less than 2x2!!!
ans = summ
for i in range(2,len(lis[0])):
    summ = summ - lis[0][i-2] - lis[1][i-2] #minus 1 column on the left
    summ = summ + lis[0][i] + lis[1][i]     #add 1 new col on the right
    ans = max(ans,summ)         #if new 2x2 mat is greater than last so update it
print(ans)
