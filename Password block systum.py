password = ""
while password != "MangluBadmas":
    password = input("Enter your password")
    if password == "MangluBadmas":
        print("Access Granted")
        break
    else:
        print("Wrong password ,Try again!")

password = "MangluBadmas"
attempts = 0
while attempts <3:
    user_input = input("Enter your password")
    if user_input == password:
        print("Access Granted ✅")
        break
    else:
        attempts +=1
        print(f"Wrong password Attempts left: {3-attempts}" )

    if attempts ==3:
        print("❌Too many wrong attempts")

    if attempts ==4:
        print("❌ Account Blocked!")
        
