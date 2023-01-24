import os
import logging
from flask import flash
import sqlite3

# WTforms module 
# add cURL functions to program

# https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
# https://itnext.io/build-a-simple-crud-todo-app-with-python-flask-in-100-lines-of-code-or-less-97d8792f24be
# https://snyk.io/advisor/python/Flask/functions/flask.request.form.get
# https://stackoverflow.com/questions/42687067/python-flask-request-args-get-returning-nonetype
# http://github.com/driscollis/flask101 -- search results (add a search form)

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr(self_):
        return "<Title: {}".format(self.id)

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
        input = request.form.get('id')
        
        if input == "ABC":
            print ("You typed ABC") # export to Visual Studio console if ABC typed in input form
        else:
            pass            # also show example of raise value error
        
        db.session.add(book)
        db.session.commit()

    books = Note.query.all() # SQLAlchemy commands

    return render_template("app_index.html", books=books)

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.form:
        #1. get Search key from request.form.get("id")
        #2. if not found, return an error.html page

        # Create a SQL connection to our SQLlite database
        input = request.form.get('id')
        con = sqlite3 = sqlite3.connect("bookdatabase.db")
        cur = con.cursor()

        ''' The result of our "cursor.execute" can be interated over by a row
        for row in cur.execute('SELECT * FROM note WHERE id="abc"'):
            print (row)
        cur.fetchall()'''

        # execute one command then make it to posts from Flask API
        posts = conn.execute('SELECT * FROM note').fetchone() # output entire DB to console
        conn.execute('DELETE FROM posts WHERE id = ?', (input,)) # this is the QUERY command
        conn.close()

        # flash('"{}" was successfully deleted!'.format(post['title'])) # flash messaging

    return render_template("search.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)