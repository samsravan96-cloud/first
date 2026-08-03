
username = "sravan"
password = "12345"

user_name = input("Enter username: ")
user_password = input("Enter password: ")
login_success = (user_name == username) and (user_password == password)
print("Login Success:", login_success)

if login_success:
    print("Welcome! Login Successful.")
else:
    print("Invalid Username or Password.")