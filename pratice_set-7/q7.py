n = int(input("enter your n value:"))
for i in range(0,n):
    print(" "* (n-(i+1)),end="")
    print("*"* (i+(i+1)),end="")
    print(" "* (n-(i+1)),end="")
    print("\n")
