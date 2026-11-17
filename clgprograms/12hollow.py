n=5
#i
for i in range(n):
    #j
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
               print("*",end="")
        else:
               print(" ",end="")
    print()
