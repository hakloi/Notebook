from file_operation import create_note, read_file, write_file
from note import Note


def add_note():
    note = create_note()
    array = read_file()
    for notes in array:
        if Note.get_id(note) == Note.get_id(notes):
            Note.set_id(note)
    array.append(note)
    write_file(array, 'a')
    print('Note added succesfully!\n')
    
    
def show(text):
    logic = True
    array = read_file()
    if text == 'date':
        date = input('Input date: dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.get_date(notes):
                print(Note.map_note(notes))
    if logic == True:
        print('There are not any notes!\n')


def id_edit_del_show(text):
    id = input('Input ID: ')
    array = read_file()
    logic = True
    for notes in array:
        if id == Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = create_note()
                Note.set_title(notes, note.get_title())
                Note.set_body(notes, note.get_body())
                Note.set_date(notes)
                print('CHANGED!\n')
            if text == 'del':
                array.remove(notes)
                print('DELETED!\n')
            if text == 'show':
                print(Note.map_note(notes))
    if logic == True:
        print('Invalid ID!!\n')
    write_file(array, 'a')
