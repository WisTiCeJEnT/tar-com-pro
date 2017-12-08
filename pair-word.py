s = input().lower()
for pair in sorted([s[i:i+2] for i in range(len(s)-1)]):
    print(pair)
