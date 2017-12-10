def namelist(lis):
    ans = ""
    if len(lis)<2:
        for s in lis:
            ans += s
        return ans
    ans += lis[0]
    for i in range(1,len(lis)-1):
        ans += f", {lis[i]}"
    ans += f" & {lis[len(lis)-1]}"
    return ans
import ast
names = ast.literal_eval(input())
print(namelist(names))
