n = int(input("enter n value:"))
for i in range(1,n+1):
    if i % 2 == 0:
        print("* *",end="")
        print("\n")
    else:
        print("*"*3,end="")
        print("\n")
