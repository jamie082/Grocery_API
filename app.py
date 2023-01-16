
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
    id = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr(self_):
        return "<Title: {}".format(self.id)

@app.route("/update", methods=["POST"]) # CRUD operations and FLASK operations
def update():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")

    if newtitle is None:
        raise EMError("Specify entry")
    else:
        pass

    if oldtitle is None:
        raise EMError("Specify entry")
    else:
        pass

    book = Note.query.filter_by(id=oldtitle).first()
    book.id = newtitle
    db.session.commit()
    return redirect("/") 

@app.route("/", methods=["GET", "POST"]) # post commands below (execute FLASK)
def home():
    if request.form:
        book = Note(id=request.form.get("id"))

        db.session.add(book)
        db.session.commit()

    books = Note.query.all() # SQLAlchemy commands

    return render_template("app_index.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)