a1,b1,c1 = (float(e) for e in  input().split())
a2,b2,c2 = (float(e) for e in  input().split())

if a1 != 0 :
  y = ((a2/a1)*c1 - c2) / (b2 - (a2/a1)*b1)
  x = -(b1*y + c1) / a1
else :
  if b1 != 0 :
    y = -c1 / b1
  else :
      print("error")
  if a2 != 0 :
      x = (b2*c1/b1 - c2) / a2
  else :
      print("error")
print(x, y)
