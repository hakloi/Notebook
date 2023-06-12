# import program as pr

# pr.run()

import csv
import datetime

class Note:
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

def save_notes():
    note_list = []
    with open('notes.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Title', 'Body', 'Date/Time'])
        for note in list_of_notes:
            note_list.append([note.id, note.title, note.body, note.date])
            writer.writerow(note_list)
    print('Notes saved to csv file')

def read_notes():
    with open('notes.csv') as f:
        reader = csv.reader(f)
        notes_list = []
        for row in reader:
            id, title, body, date = row[0:4]
            notes_list.append(Note(id, title, body, date))
        return notes_list

def add_note():
    title = input('Enter title: ')
    body = input('Enter body: ')
    date = datetime.datetime.now()
    note = Note(0, title, body, date)
    list_of_notes.append(note)
    save_notes()
    print('Note added')

def edit_note():
    id = input('Enter the ID of note to edit')
    note = Note(id, input('Enter new title: '), input('Enter new body: '), datetime.datetime.now())
    list_of_notes[id] = note
    save_notes()
    print('Note modified')        
               
    while True:
        choice = input('Enter the command (a - add, e - edit, d - delete, r - read, s - save, q - quit): ')
        if choice.lower() == 'a':
            add_note()
        elif choice.lower() == 'e':
            edit_note()
        elif choice.lower() == 'd':
            delete_note()
        elif choice.lower() == 'r':
            read_notes()
        elif choice.lower() == 's':
            save_notes()
        elif choice.lower() == 'q':
            print('Thanks for using this app')
            break
        else:
            print('Invalid command')
