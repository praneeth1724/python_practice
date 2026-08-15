def remove_listitem(word,l):
    l.remove(word)

user_input = input("enter your names:")
names = user_input.split()
rm = input("enter name that you want to remove:")
print(names)
remove_listitem(rm,names)
print(names)
