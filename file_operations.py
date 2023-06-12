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
    notes.append(note_new)
    print(f"Note created with id: {note_new.get_id()}")
    print(notes)
    # save_note(note)

def read_note():
    # take header 
    # edit body
    print()
    
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