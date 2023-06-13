import datetime
import uuid

notes = []

class Note:
    def __init__(self, id = str(uuid.uuid1())[0:2], title = "", body = "", date = str(datetime.date.today().strftime("%d.%m.%Y"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date
        
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_date(self):
        return self.date

    def set_id(self):
        self.id = str(uuid.uuid1())[0:2]

    def set_title(self, title):
        self.title = title

    def set_body(self, body):
        self.body = body

    def set_date(self):
        self.date = str(datetime.date.today().strftime("%d.%m.%Y"))
    
    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def map_note(note):
        return '\nID: ' + note.id + '\n' + 'Название: ' + note.title + '\n' + 'Описание: ' + note.body + '\n' + 'Дата публикации: ' + note.date