num = int(input("enter to check the number is a prime number or not:"))
ni = "prime number"
for i in range(2,int(num**0.5)+1):
    if num % i == 0:
        ni = "not a prime number"
    else:
        ni
print(ni)
