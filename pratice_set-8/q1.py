def to_find_greatest_num(a,b,c):
    if(a>b and a>c):
        print(a,"is the greatest number among the three numbers")
    elif(b>c):
        print(b,"is the greatest number among the three numbers")
    else:
        print(c,"is the greatest number among the three numbers")

x = int(input("enter your first number:"))
y = int(input("enter your second number:"))
z = int(input("enter your third number:"))
to_find_greatest_num(x,y,z)
