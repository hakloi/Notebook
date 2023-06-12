import datetime
import uuid

notes = []

class Note:
    def __init__(self, id = "", title = "", body = "", date = ""):
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

    def set_id(self, new_id):
        self.id = str(uuid.uuid1())[0:6]

    def set_title(self, new_title):
        self.title = new_title

    def set_body(self, new_body):
        self.body = new_body

    def set_date(self, new_date):
        self.date = str(datetime.date.today().strftime("%d.%m.%Y"))
        
    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date
