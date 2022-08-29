from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired 
from flask_wtf import FlaskForm


class InputStudents(FlaskForm):
    students_name = StringField('Nama Panggilan', validators=[DataRequired()])
    students_fullname = StringField('Nama Lengkap', validators=[DataRequired()])
    students_gender = RadioField(choices = [('L', 'Laki-Laki'), ('P', 'Perempuan')])
    students_address = TextAreaField('Alamat', validators=[DataRequired()])
    submit_form = SubmitField('Kirim')

class InputViolation(FlaskForm):
    students_violation = TextAreaField('Pelanggaran', validators=[DataRequired()])
    submit_form_2 = SubmitField('Tambah')