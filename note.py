class Note:
    def __init__(self, id, title, body, date):
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
        self.id = new_id

    def set_title(self, new_title):
        self.title = new_title

    def set_body(self, new_body):
        self.body = new_body

    def set_date(self, new_date):
        self.date = new_date