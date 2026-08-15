spam =["make a lot of money","buy now","subscribe this","click this"]
a = input("enter your msg:")
status = "true cmt"
if a in spam:
    status = "false cmt"

print(status)
