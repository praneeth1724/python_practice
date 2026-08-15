def re_sumofn(n):
    if n == 1:
        return n
    else:
        return n + re_sumofn(n-1)

num = int(input("enter n value to find sum of n numbers:"))
print("sum of n natural numbers is:",re_sumofn(num))
