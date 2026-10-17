while True:
    print("____Prime Number Menu_____")
    print("1.check Prime number")
    print("2.generate prime number")
    print("3.exit")
    choice = int(input("enter your choice"))
    match choice:
        case 1:
            n = int(input("enter a number"))
            if n <= 1:
                print("not a prime number")
            else:
                count = 0 
                for i in range(1,n+1):
                    if n%i == 0:
                        count += 1
                if count == 2:
                    print(n,"is a prime number")
                else:
                    print(n,"is not a prime number")
        case 2:
            limit = int(input("enter the limit"))
            for n in range(2,limit+1):
                count = 0
                for i in range(1,n+1):
                     if n%i == 0:
                        count += 1
                if count == 2:
                    print(n,end=" ")
            print()
        case 3:
            print("program terminated")
            break

