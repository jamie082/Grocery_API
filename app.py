
import os 


# https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
# https://itnext.io/build-a-simple-crud-todo-app-with-python-flask-in-100-lines-of-code-or-less-97d8792f24be

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

@app.route("/", methods=["GET", "POST"]) # CRUD and SQLALchemy operations
def home():
    if request.form == "POST":
        # access "title" from app_index.html
        grocery = Note(request.form.get(id=request.form.get("title")))

    # load web site and issue query command to DB

    notes = Note.query.all()
    return render_template("app_index.html", notes=notes)

def create_note(text):
    note = Note(text=text)
    
    # database commands SQLAlchemy
    db.session.add(note)
    db.session.commit()
    db.session.refresh(note)

def read_notes():
    return db.session.query(Note).all()

@app.route("/", methods=["POST", "GET"]) # post commands below (execute FLASK)
def view_index():
    if request.method == "POST":
        create_note(request.form['title'])
        
    return render_template("app_index.html", notes=read_notes())
        
    # SQLALchemy commands

@app.route("/update", methods=["POST"]) # CRUD operations and FLASK operations
def update():
    db.session.query(Note).update() # SQLAlchemy commands

def delete_note():
    db.session.query(Note).filter_by(id=note_id).delete() # SQLAlchemy commands

if __name__ == "__main__":
    app.run(debug=True)