a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b:
    if a>c:
        print("greatest number is",a)
    else:
        print("greatest number is",c)
else:
    if b>c:
        print("greatest number is",b)
    else:
        print("greatest number is",c)