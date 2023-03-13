import json
from menu import Menu


class Registration:
    @staticmethod
    def sign_in():
        print("[ Sign_in ]".center(70, '-'))
        username = str(input('username: '))
        password = str(input('password: '))

        with open("Data_base/User_pass.json", 'r') as file:
            data = json.loads(file.read())

        if username in [i['username'] for i in data]:
            for user in data:
                if (user['username'] == username) and (user['password'] == password):
                    print(f"[ {username}'s diary ]".center(70, '-'))
                    Menu().run()

                elif (user['username'] == username) and (user['password'] != password):
                    print('password not correct, try log in again')
                    Registration.sign_in()

        else:
            print(f'user {username} not registered')
            Registration.sign_in()

    @staticmethod
    def sign_up():
        print("[ Registration ]".center(70, '-'))
        print('enter username and password, min 4 simbols')
        new_user = str(input('username: '))

        with open("Data_base/User_pass.json", 'r') as file:
            data = json.loads(file.read())

        if new_user in [i['username'] for i in data]:
            print("user with this username already exist, chose another")
            Registration.sign_up()

        else:
            new_password = str(input("new password: "))

            while len(new_password) < 4:
                new_password = str(input("new password: "))

            data.append({"username": str(new_user), "password": str(new_password)})
            with open("Data_base/User_pass.json", 'w') as update:
                json.dump(data, update)

            personal_file = f"Data_base/{new_user}.txt"

            with open(personal_file, 'w') as personal_file:
                personal_file.write(f"username: {new_user} \n\nDiary: \n\n")
            print('[ You are successfully registered ]'.center(70, '-'))
            Registration.Registration_menu()

    @staticmethod
    def Registration_menu():
        print("""
            For registration press ----- [ R ]
            For sign_in press ---------- [ S ]
            Incognito ------------------ [ I ]
            
            [ Incognito diary not secured and may be lost ]
        """)
        move = str(input('▁ ')).upper()
        if move == 'R':
            Registration.sign_up()
        elif move == 'S':
            Registration.sign_in()
        elif move == 'I':
            Menu().run()
        else:
            print('try again')
            Registration.Registration_menu()


if __name__ == "__main__":
    Registration.Registration_menu()
