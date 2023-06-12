import csv
import note
from note import *
import pandas as pd

def create_note():
    title = input("Title: ")
    body = input("Body: ")
    id = str(uuid.uuid1())[0:3]  # generate a unique ID
    date = datetime.date.today  # get the current day
    note_new = Note(id, title, body, date)
    print(f"---\nTitle: {note_new.title} \nBody: {note_new.body} \nID: {note_new.id} \nDate: {note_new.date} \n---")
    notes.append(note_new)
    print(f"Note created with id: {note_new.get_id()}")
    # save_note(note)

def read_note(file_path, id):
    with open('note1.csv', 'r') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)

        for row in csv_reader:
            if row[0] == id:
                new_note = Note(id, row[1], row[2], row[3], row[4])
                return new_note
    return None
    
def write_note():
    # header 
    # body
    print()
    
def edit_note():
    # take header
    # edit body
    print()

def delete_note():
    # take header
    print()
    
def save_note(id):
    note = Note(title, body, date)
    notes.append(note)
    print("Note saved with id:", note.get_id)
    return note.get_id