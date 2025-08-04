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
while attempts <6:
    user_input = input("Enter your password")
    if user_input == password:
        print("Access Granted ✅")
        break
    else:
        attempts +=1
        print(f"Wrong password Attempts left: {6-attempts}" )

    if attempts ==3:
        print("❌Too many wrong attempts")

    if attempts ==4:
        print(f"Your account will be blocked at {attempts +2}")

    if attempts >=6:
        print("❌ Account Blocked!")
        
