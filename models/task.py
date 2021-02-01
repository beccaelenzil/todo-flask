from main import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(255))
    complete = db.Column(db.Boolean)

    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content
        self.complete = False

    def __repr__(self):
        return '<Task %s>' % self.title

    def make_json(self):
        return {
            'title': self.title, 
            'content': self.content, 
            'id': self.id, 
            'complete': self.complete
            }