def sum(n):
  if n <=1 :
    return n
  else :
      return n+sum(n-1)

imp= int(input("enter your number : "))
print("sum is : " ,sum(imp))

