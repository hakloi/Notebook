# import csv
from note import *
# import pandas as pd

def create_note():
    title = input("Title: ")
    body = input("Body: ")
    # # id = str(uuid.uuid1())[0:3]  # generate a unique ID
    # # date = note.datetime()
    # note_new = Note(id, title, body)
    # print(f"---\nTitle: {note_new.title} \nBody: {note_new.body} \nID: {note_new.id} \nDate: {note_new.date} \n---")
    # notes.append(note_new)
    # print(f"Note created with id: {note_new.get_id()}")
    # # save_note(note)
    return Note(title=title, body=body)

def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.to_string(notes))
        file.write('\n')
    file.close


def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array



# def write_note():
#     # header 
#     # body
#     print()
    
# def edit_note():
#     # take header
#     # edit body
#     print()

# def delete_note():
#     # take header
#     print()
    
# def save_note(id):
#     note = Note(title, body, date)
#     notes.append(note)
#     print("Note saved with id:", note.get_id)
#     return note.get_id