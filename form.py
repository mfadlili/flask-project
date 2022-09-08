from wtforms import StringField, SubmitField, TextAreaField, PasswordField, RadioField, IntegerField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf import FlaskForm
from models import User


class InputStudents(FlaskForm):
    students_name = StringField('Nama Panggilan', validators=[DataRequired()])
    students_fullname = StringField('Nama Lengkap', validators=[DataRequired()])
    students_gender = RadioField(choices = [('L', 'Laki-Laki'), ('P', 'Perempuan')])
    students_address = TextAreaField('Alamat', validators=[DataRequired()])
    submit_form = SubmitField('Kirim')

class InputViolation(FlaskForm):
    students_violation = TextAreaField('Pelanggaran', validators=[DataRequired()])
    setudent_add_point = IntegerField('Point Pelanggaran', validators=[DataRequired()])
    submit_form_2 = SubmitField('Tambah')

class DeleteStudents(FlaskForm):
    id_delete = IntegerField('Ketik Id Siswa', validators=[DataRequired()])
    submit_form_2 = SubmitField('Hapus')

class LoginUser(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password: ',  validators=[DataRequired()]) 
    submit = SubmitField('Login')

class RegisterUser(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ',  validators=[DataRequired()]) 
    password2 = PasswordField('Retype Password: ',  validators=[DataRequired(), EqualTo('password')]) 
    submit = SubmitField('Register')

    def check_username(self, username):
        if User.query.filter_by(username=username.data).first():
            return ValidationError('Username already taken')
    
    def check_email(self, email):
        if User.query.filter_by(email=email.data).first():
            return ValidationError('Email already taken')