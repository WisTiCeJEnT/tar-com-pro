def sumD(n):
    ans = 0
    while n>0:
        ans += n%10
        n = n//10
    return ans
inp = int(input())
while inp > 9:
    inp = sumD(inp)
print(inp)
