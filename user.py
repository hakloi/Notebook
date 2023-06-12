import csv
from file_operations import edit_note, read_note, delete_note, save_note
import note


def start():
    while True:
        print("Welcome to Notes Console Application!")
        print("Please choose an option:")
        print("1. Add a new note")
        print("2. Edit an existing note")
        print("3. Delete an existing note")
        print("4. Read all notes")
        print("5. Save the notes as a CSV file")
        choice = input("Enter your choice: ")

        if choice == "1":
            note_id = int(input("Enter the note ID: "))
            title = input("Enter the title: ")
            body = input("Enter the body: ")
            date = input("Enter the date: ")
            note = note.Note(note_id, title, body, date)
            save_note(note)
        elif choice == "2":
            note_id = int(input("Enter the note ID: "))
            title = input("Enter the new title: ")
            body = input("Enter the new body: ")
            date = input("Enter the new date: ")
            edit_note(note_id, title, body, date)
        elif choice == "3":
            note_id = int(input("Enter the note ID to delete: "))
            delete_note(note_id)
        elif choice == "4":
            read_note()
        elif choice == "5":
            with open("notes.csv", "w", newline="") as f:
                writer = csv.writer(f)
                for note in notes:
                    writer.writerow([note.get_id(), note.get_title(), note.get_body(), note.get_date()])
            print("Notes saved as a CSV file.")
        else:
            print("Invalid choice. Please try again.")
