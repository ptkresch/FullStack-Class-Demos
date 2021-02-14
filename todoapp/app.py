from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://prestonkresch:password@localhost:5432/todoapp'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__='todoapp'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    def __repr__(self):
        return f'<Todo {self.id}, {self.description}>'

# db.create_all()


#AJAX implementation
@app.route('/todos/create', methods=['POST'])
def create_todo(): 
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        #Trigger an error
        # todo = Todo(description2=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except: 
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify(body)



#Form submission
# @app.route('/todos/create', methods=['POST'])
# def create_todo(): 
#     description = request.form.get('description', '')
#     todo = Todo(description=description)
#     db.session.add(todo)
#     db.session.commit()
#     return redirect(url_for('index'))


#index looks for this default path
@app.route('/')

def index(): 
    #By default, Flask looks for templates in project directory called "templates"
    return render_template('index.html', data = Todo.query.all())
    # Instead of data returned manually, use the Todo object to query the data
    # data=[{'description': 'Todo 1'}, {'description': 'Todo 2'}, {'description': 'Todo 3'}, {'description': 'Todo 4'}])
if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)