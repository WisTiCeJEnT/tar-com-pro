def namelist(lis):
    ans = ""
    if len(lis)<2:
        for s in lis:
            ans += s
        return ans
    #print(lis[0])
    ans += lis[0]
    i = 1
    while i<len(lis)-1:
        #print(f", '{lis[i]}'",end='')
        ans += f", {lis[i]}"
        i += 1
    #print(f" & {lis[i]}")
    ans += f" & {lis[i]}"
    return ans
import ast
names = ast.literal_eval(input())
print(namelist(names))
