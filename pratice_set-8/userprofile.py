def create_user_profile(username, *roles , **metadata):
    users = {"user" : username, "roles" : (roles), "metadata" : metadata}
    return users

username = input("enter your username:")
sec = input("enter your security clearance position:")
role = input("enter your work role:")
mail = input("enter your mail id:")
loc = input("enter your location:")

user1 = create_user_profile(username, sec,role ,email=mail,location=loc)
print("user created successfully")
print(f"username is {user1["user"]}")
ri = user1.get("roles")
print(f"Your roles are \n1.The security clearance your in {ri[0]} \n2.Your role is {ri[1]}")
print(f"Your given mail id is {user1.get("metadata", {}).get("email")}")
print(f"Your location is {user1.get("metadata", {}).get("location")}")

