st = int(input("enter start of limit:"))
en = int(input("enter end of limit:"))
for n in range(st,en+1):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count += 1
    if count == 2:
        print(n,end=" ")

