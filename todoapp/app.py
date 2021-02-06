from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://prestonkresch:password@localhost:5432/todoapp'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__='todoapp'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id}, {self.description}>'

db.create_all()

#index looks for this default path
@app.route('/')

def index(): 
    #By default, Flask looks for templates in project directory called "templates"
    return render_template('index.html', data = Todo.query.all())
    # Instead of data returned manually, use the Todo object to query the data
    # data=[{'description': 'Todo 1'}, {'description': 'Todo 2'}, {'description': 'Todo 3'}, {'description': 'Todo 4'}])
if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)