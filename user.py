# import csv
# from file_operation import edit_note, delete_note
# from note import notes
from operation import add_note, id_edit_del_show, show 


def start():
    while True:
        print("Welcome to Notes Console Application!")
        print("Please choose an option:")
        print("1. Add a new note")
        print("2. Edit an existing note")
        print("3. Delete an existing note")
        print("4. Read all notes")
        print("5. Save the notes as a CSV file")
        print("6. Exit")
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
            
        # elif choice == "5":
            # with open("notes.csv", "w", newline="") as f:
            #     writer = csv.writer(f)
            #     for note in notes:
            #         writer.writerow([note.get_id(), note.get_title(), note.get_body(), note.get_date()])
            # print("Notes saved as a CSV file.")
            
        elif choice == "6":
            print("Goodbye! Have a good day!")
            break
        else:
            print("Invalid choice. Please try again.")
