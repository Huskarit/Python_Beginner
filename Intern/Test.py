from flask import Flask, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators

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

#db.create_all()
#db.session.commit()

#Insert
@app.route('/', methods = ['GET', 'POST'])
def student():
    if request.method == "POST":
        details = request.form
        ID = details['ID']
        name = details['name']
        gender = details['gender']
        age = details['age']
        DOB = details['DOB']
        email = details['email']
        try:
            new_st = students(ID, name, gender, age, DOB, email)
            db.session.add(new_st)
            db.session.commit()
        except:
            return '<h1> Add Unsuccessfully </h1>'
        return '<h1> Add Successfully </h1>' 
    return render_template('student.html')

#using ID to delete student
@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    if request.method == "POST":
        details = request.form
        id_del = details['ID']
        try:
            delete_st = students.query.filter_by(ID = id_del).first()
            db.session.delete(delete_st)
            db.session.commit()
        except Exception as e:
            return str(e)
        return '<h1> Delete Successfully </h1>'
    return render_template('delete.html')   

#using ID to show student
@app.route('/show', methods = ['GET', 'POST'])
def show():
    if request.method == "POST":
        details = request.form
        id_show = details['ID']   
        info_st = students.query.filter_by(ID = id_show).first()
        return render_template('show_student.html', info_st = info_st)
    return render_template('show.html')

#show all students
@app.route('/show_all')
def show_all():
    info_st = students.query.all()
    print(info_st)
    return render_template('show_student.html', info_st = info_st)

#using ID to update information of student
@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == "POST":
        details = request.form
        ID = details['ID']
        name = details['name']
        gender = details['gender']
        age = details['age']
        DOB = details['DOB']
        email = details['email']
        info_st = students.query.filter_by(ID = ID).first()
        print(info_st)
        if name != '':
            info_st.name = name
        if gender != '':
            info_st.gender = gender
        if age != '':
            info_st.age = age
        if DOB != '':
            info_st.DOB = DOB
        if email != '':
            info_st.email = email
        db.session.commit()
        return '<h1> Update Successfully </h1>'
    return render_template('update.html')

if __name__ == '__main__':
    app.run()