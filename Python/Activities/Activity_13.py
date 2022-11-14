def sum(*num) :
    plus= 0
    for i in num :
      print(type(i))
      k=int(i)
      plus= plus + k 
    print(plus)

numbers=input("enter your number seperated by a comma : ")
print(numbers)
print(numbers[0])
sum(numbers)