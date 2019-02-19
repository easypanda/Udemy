import os
from forms import AddForm, DelForm

from flask import Flask,render_template,url_for,redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')

db = SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):

    __tablename__ = "puppies"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Puppy name: {self.name}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add",methods=["GET","POST"])
def add_pup():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for("list_pup"))

    return render_template("add_puppies.html",form=form)

@app.route("/list")
def list_pup():

    puppies = Puppy.query.all()
    return render_template("list.html",puppies=puppies)

@app.route("/delete",methods = ["GET","POST"])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for("list.html"))
    return render_template("delete_puppies.html",form=form)

if __name__ == "__main__":
    app.run(debug=True)
