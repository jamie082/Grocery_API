import os
import logging
import flash

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
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr(self_):
        return "<Title: {}".format(self.id)
'''
class DB(db.Model):
    name = db.Column(db.String)
'''
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


# https://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/
# https://flask.palletsprojects.com/en/2.2.x/patterns/flashing/

@app.route("/results", methods=["GET"]) # 
def search():
    results = []
    search_string = search.data['id'] # search form in name='id'

    if search.data['id'] == '':
        qry = db.session.query(Note).all() # SQKAlchemy
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')

    else:
        # display results

        return render_template('search.html', qry=qry)

if __name__ == "__main__":
    app.run(debug=True)