arr = [7,8,25,1,25]
minval = arr[0]
for ele in arr:
    if minval > ele:
        minval = ele
print("lowest element is:",minval)
