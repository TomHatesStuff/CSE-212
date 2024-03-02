
# 1. Name:
#      Luke Marshall
# 2. Assignment Name:
#      Lab-02_Authentication
# 3. Assignment Description:
#      take a username and passwordc use a json list and say if you are authenticated
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part most definitly was the json file. FIrst there was an extra quotation maark that messed with the program a bit. And lastly it wouldnt work no matter what until i restarted it.
# 5. How long did it take for you to complete the assignment?
#      5 hours
import json

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Unable to open file {filename}.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file {filename}.")
        return None

def convert_to_lists(json_data):
    if json_data:
        usernames = json_data.get("username", [])
        passwords = json_data.get("password", [])
        return usernames, passwords
    return [], []

def authenticate_user(username, password, usernames, passwords):
    if username in usernames and password in passwords:
        index = usernames.index(username)
        if passwords[index] == password:
            return True
    return False

def main():
    filename = "Lab02.json"
    json_data = read_file(filename)

    if json_data is not None:
        usernames, passwords = convert_to_lists(json_data)

        username_input = input("Username: ")
        password_input = input("Password: ")

        if authenticate_user(username_input, password_input, usernames, passwords):
            print("You are authenticated!")
        else:
            print("You are not authorized to use the system.")

if __name__ == "__main__":
    main()
