from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin1999@localhost/Management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class students(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    DOB = db.Column(db.Date)
    email = db.Column(db.String(50))

    def __init__(self, ID, name, gender, age, DOB, email):
        self.ID = ID
        self.name = name
        self.gender = gender
        self.age = age
        self.DOB = DOB
        self.email = email

db.create_all()
db.session.commit()
