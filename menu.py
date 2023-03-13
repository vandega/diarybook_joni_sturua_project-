import sys

from diarybook import DiaryBook
from util import read_from_json_into_application


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

    def display_menu(self):
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

    def show_diaries(self, diaries=None):
        if not diaries:
            diaries = self.diarybook.diaries
        for diary in diaries:
            print(f"{diary.id}-{diary.memo}")

    def add_diary(self):
        print(self.username, self.password)

        with open(f'Data_base/{self.username}.txt', 'a') as textfile:
            textfile.write((str(input())))
            textfile.write('\n')
            print('For tags use [ , ]\nTags :', end="")
            textfile.write((str(input())))
            textfile.write('\n\n')

        # self.diarybook.new_diary(memo, tags)
        print("Your note has been added")

    def search_diaries(self):

        filter_text = input("Search for:  ")
        diaries = self.diarybook.search_diary(filter_text)
        for diary in diaries:
            print(f"{diary.id}-{diary.memo}")

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
