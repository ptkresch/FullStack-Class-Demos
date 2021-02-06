from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://prestonkresch:password@localhost:5432/example2'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# optional - postgresql+psycopg2://username:password@ip_address:port/db_name
# python app using postgress defaults to psycopg2

db = SQLAlchemy   (app) #instance of database
#db.model is an object that lets us create and manipulate models
#Models are defined as classes, which map to tables in our database
#db.session lets us create and manipulate transactions and the context of a session 
    ##used to interact with a database

#Sets table name to lowercase version of class by default
#To set a custom name, add __tablename__ = 'people'
#Typically, you set an init method - SQLAlchemy takes care of this for you.
class Person(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'

#db.create_all() detects models and creates tables for them if they don't exist 
#db.create_all() doesn't recreate existing models - no overwrite of data!

db.create_all()


@app.route("/")

def index():
    person = Person.query.first()
    return "Hello " + person.name

if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)