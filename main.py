from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
db.init_app(app)

seeder = FlaskSeeder()
seeder.init_app(app, db)

# -- to drop the database in python3---
# from main import db
# db.drop_all()
# db.create_all()

# model
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

def make_json(task):
    return {
        'title': task.title, 
        'content': task.content, 
        'id': task.id, 
        'complete': task.complete
        }

# controller
@app.route('/task/<task_id>', methods=['GET', 'DELETE', 'PATCH'])
def task(task_id):
    if request.method == 'GET':
        task = Task.query.get_or_404(task_id)
        return make_json(task)
    elif request.method == 'PATCH':
         task = Task.query.get_or_404(task_id)

         if 'title' in request.json:
             task.title = request.json['title']
         if 'content' in request.json:
             task.content = request.json['content']

         db.session.commit()
         return make_json(task)

    elif request.method == 'DELETE':
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return '', 204

@app.route('/', methods=['GET'])
@app.route('/tasks', methods=['POST', 'GET'])
def tasks():
    if request.method == 'GET':
        tasks = Task.query.all()
        tasks_list = []
        for task in tasks:
            tasks_list.append(make_json(task))
        return jsonify(tasks_list) 
    elif request.method == 'POST':
        new_task = Task(
            title=request.json['title'],
            content=request.json['content']
        )
        db.session.add(new_task)
        db.session.commit()
        return make_json(new_task)

if __name__ == '__main__':
    app.run(debug = True)