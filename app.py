import os
import logging

# add cURL functions to program

# https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
# https://itnext.io/build-a-simple-crud-todo-app-with-python-flask-in-100-lines-of-code-or-less-97d8792f24be
# https://snyk.io/advisor/python/Flask/functions/flask.request.form.get

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
    id = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr(self_):
        return "<Title: {}".format(self.id)

class DB(db.Model):
    name = db.Column(db.String)

@app.route("/update", methods=["POST"]) # CRUD operations and FLASK operations
def update():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")

    book = Note.query.filter_by(id=oldtitle).first()
    book.id = newtitle
    db.session.commit()
    return redirect("/") 

@app.route("/", methods=["GET", "POST"]) # post commands below (execute FLASK)
def home():
    if request.form:
        book = Note(id=request.form.get("id"))

        input = request.form['id']
        if input == "ABC":
            print ("You typed ABC")
        else:
            pass            # also show example of raise value error
        
        db.session.add(book)
        db.session.commit()

    books = Note.query.all() # SQLAlchemy commands

    return render_template("app_index.html", books=books)

@app.route("/search", methods=["GET"])
def search():

    # https://python-adv-web-apps.readthedocs.io/en/latest/flask_db2.html

    try:
        query = request.args.get("id") # get input from web form in app_index.html
        db_search = DB.query.filter_by(style='')
        db.session.add(db_search)
        db.session.commit()

    found = DB.query.all()

    return render_template("search.html", found=found)

if __name__ == "__main__":
    app.run(debug=True)