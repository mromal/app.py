from flask import Flask, render_template
from flask_sqlalchemy import SQLAchemy

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mohaiyudinromal@localhost:5432/todoapp'
db = SQLAchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)

    def __init__(self):
        return f'<Todo {self.id}{self.description}>'

db.create_all()

@app.route('/')
def index():
   return render_template ('index.html', data=Todo.query.all()
   )
