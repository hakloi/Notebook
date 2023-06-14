import os
import time
from operation import add_note, id_edit_del_show, show 


def start():
    while True:
        print("Welcome to Notes Console Application!")
        print("Please choose an option:")
        print("1. Add a new note")
        print("2. Edit an existing note")
        print("3. Delete an existing note")
        print("4. Read all notes")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()
            
        elif choice == "2":
            show('all')
            id_edit_del_show('edit')
            
        elif choice == "3":
            show('all')
            id_edit_del_show('del')
            
        elif choice == "4":
            show('id')
            id_edit_del_show('show')
            
        elif choice == "5":
            print("Goodbye! Have a good day!")
            # ПОСТАВИТЬ ТАЙМЕР 6 СЕКУННД
            time.sleep(2)
            clear = lambda: os.system('cls')
            clear()
            break
        else:
            print("Invalid choice. Please try again.")
