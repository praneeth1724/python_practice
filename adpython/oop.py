import js 
class login:
    def __init__(self,name,passw):
        for user in users:
            if(name == user):
                    if(users.get(name) == passw):
                        print("login successfull")
                    else:
                        print("incorrect password")
                    break    
            elif(name != user):
                print("user not found")


users = { "praneeth" : "1724" , "xyz" : "1234"}
up =  input("enter your name:")
pw = input("enter your password:")
login(up,pw)
js.to_dump(users,"users.json")
