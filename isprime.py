n = int(input())
Prime = True
for i in range(2,int(n**(1/2))+1):
    if n%i==0:
        Prime = False
print(Prime) 
