is_authenticated = False
access_token = ""

while not is_authenticated:
    username = input("Username:")
    password = input("Password:")

    if username == "parsa" and password == "123456":
        is_authenticated = True
        access_token = "afdfsafsafdhsafasfsa.dfasfafsafafd.dfasfsafsa"
        print("You logged in successfully")
    else:
        print("User not found")

print(access_token)