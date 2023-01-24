import os
import logging
from flask import flash
import sqlite3

# WTforms module 
# add cURL functions to program

# add cURL output

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

    def __repr(self):
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
            input = request.form.get('search')
            con = sqlite3.connect("bookdatabase.db")
            cur = con.cursor()

            id_select = ('input',)
            #posts = con.execute('SELECT * FROM note WHERE id=?', id_select).fetchall()
            posts = con.execute('SELECT * from note').fetchall()
            
            print("An error occured")

            return render_template("search.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)