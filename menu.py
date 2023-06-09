import sys
from diarybook import DiaryBook
from util import read_from_json_into_application
import json
import os


class Menu:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.diarybook = DiaryBook()

        self.choices = {
            "1": self.show_diaries,
            "2": self.add_diary,
            "3": self.search_diaries,
            "4": self.populate_database,
            '5': self.quit
        }

    @staticmethod
    def display_menu():
        print(""" 
        |============[ NOTEBOOK MENU ]===========|  
        |   SHOW DIARIES --------------- [ 1 ]   |
        |   ADD DEARY ------------------ [ 2 ]   |
        |   SEARCH DIARIES ------------- [ 3 ]   |
        |   Populate database ---------- [ 4 ]   |
        |   QUIT ----------------------- [ 5 ]   |
        |========================================|
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_diaries(self):
        file_path = f'Data_base/{self.username}.json'

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                context = json.load(file)
                for diary in context:
                    print(diary)

        else:
            print('no diary')


    def add_diary(self):
        print(self.username, self.password)

        text = str(input('text: '))
        tag = str(input("tag: "))

        data = [{'text': text, 'tag': tag}]

        file_path = f'/home/user/Desktop/diarybook_joni_sturua_project-/Data_base/{self.username}.json'

        if os.path.exists(file_path):
            print('if')
            with open(file_path, 'r') as file:
                existing_data = json.load(file)

        else:
            print('else')
            existing_data = []

        existing_data.extend(data)

        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=4)

        print('added successfully ')

    def search_diaries(self):

        # filter_text = input("Search for:  ")
        # diaries = self.diarybook.search_diary(filter_text)
        # for diary in diaries:
        #     print(f"{diary.id}-{diary.memo}")

        search = str(input("search: "))
        # now it opens file for current user and dinds in its personal file:
        with open(f'Data_base/{self.username}.json', 'r') as file:
            data = json.load(file)
            for i in data:
                if search in i['text'] or search in i['tag']:
                    print(i)


    @staticmethod
    def quit():
        print("Thank you for using diarybook today")
        sys.exit(0)

    def populate_database(self):
        diaries1 = read_from_json_into_application('data.json')
        for diary in diaries1:
            self.diarybook.diaries.append(diary)


if __name__ == "__main__":
    Menu().run()
