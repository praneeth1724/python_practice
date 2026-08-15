spam = ["make a lot of money", "buy now", "subscribe this", "click this"]
a = input("enter your msg: ") # FIXED: Removed the brackets [] around input

status = "true cmt"

if a in spam: # FIXED: Flipped 'spam in a' to 'a in spam'
    status = "false cmt"

print(status)
