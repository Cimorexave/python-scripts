import json

file = open("admint.txt", "r")
file = json.load(file)

input_username = input("Enter Username: ")
input_password = input("Enter Password: ")

for admin in file:
	if admin['username'] == input_username and admin['password'] == input_password:
		print("Logged In ")
	else: 
		print("Wrong Password")
