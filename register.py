import sys
import json
import importlib
import menu


class Register:

    def __init__(self):
        self.username = input('Username: ')
        self.password = input('password: ')


    def user(self):
        self.sign_in(self.username, self.password)

    def sign_in(self, username, password):
        self.username = username
        self.password = password

        with open("Data_base/User_pass.json", 'r') as file:
            data = json.loads(file.read())

        if username in [i['username'] for i in data]:
            for user in data:
                if (user['username'] == username) and (user['password'] == password):
                    print(f"[ {username}'s diary ]".center(70, '-'))
                    importlib.import_module(menu.Menu(username, password).run())

                elif (user['username'] == username) and (user['password'] != password):
                    print('password not correct, try log in again')
                    Register().user()

        else:
            print(f'user {username} not registered')
            Register.registration_menu()

    def new_user(self):
        self.sign_up(self.username, self.password)

    def sign_up(self, username, password):
        self.username = username
        self.password = password

        with open("Data_base/User_pass.json", 'r') as file:
            data = json.loads(file.read())

        if self.username in [i['username'] for i in data]:
            print("user with this username already exist, chose another")
            self.username = str(input('username: '))
            Register.sign_up(self, username, password)

        else:

            while len(self.password) < 4:
                self.password = str(input("new password: "))

            data.append({"username": str(self.username), "password": str(self.password)})
            with open("Data_base/User_pass.json", 'w') as update:
                json.dump(data, update)

            personal_file = f"Data_base/{self.username}.txt"

            with open(personal_file, 'w') as personal_file:
                personal_file.write(f"username: {self.username} \n\nDiary: \n\n")
            print('[ You are successfully registered ]'.center(70, '-'))
            Register.registration_menu()

    @staticmethod
    def registration_menu():
        print("""
        |================[ MENU ]================|
        |   REGISTRATION --------------- [ R ]   |
        |   SIGN UP -------------------- [ S ]   |
        |   QUIT ----------------------- [ Q ]   |
        |========================================|
        """)

        move = input('ANSWER  : ').upper()
        if move == 'R':
            print("[ Registration ]".center(70, '-'))
            print('enter username and password, min 4 simbols')
            Register().new_user()
        if move == "S":
            Register().user()
        if move == "Q":
            sys.exit()


if __name__ == "__main__":
    Register.registration_menu()
