tuple1= tuple(input("enter your tuple seperated by a comma: ").split(","))
print(tuple1)
for i in tuple1 :
    print(type(i))
    if (int(i)%5==0) :
      print(i)
 