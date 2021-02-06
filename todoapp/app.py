from flask import Flask, render_template

app = Flask(__name__) #named after name of our file

#index looks for this default path
@app.route('/')
def index(): 
    #By default, Flask looks for templates in project directory called "templates"
    return render_template('index.html', data=[{
        'description': 'Todo 1'
    }, {
        'description': 'Todo 2'
    }, {
        'description': 'Todo 3'
    }, {
        'description': 'Todo 4'
    }])
