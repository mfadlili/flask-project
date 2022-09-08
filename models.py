from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Students(db.Model):

    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    full_name = db.Column(db.Text)
    address = db.Column(db.Text)
    gender = db.Column(db.Text)
    #One to many relationship (a student can have many violations)
    violations = db.relationship('Violation', backref='student', lazy='dynamic')

    def __init__(self, name, full_name, address, gender):
        self.name = name
        self.full_name = full_name
        self.address = address
        self.gender = gender

class Violation(db.Model):
    
    __tablename__ = 'violations'

    id = db.Column(db.Integer, primary_key=True)
    violation = db.Column(db.Text)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    point = db.Column(db.Integer)

    def __init__(self, violation, student_id, point):
        self.violation = violation
        self.student_id = student_id
        self.point = point