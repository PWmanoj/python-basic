a=int(input("enter the number rows:"))
for i in range(0,a):
    for j in range(0,a-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end="")
    print()