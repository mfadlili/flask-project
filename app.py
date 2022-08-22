from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired 


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

class InputStudents(FlaskForm):
    students_name = StringField('Nama Panggilan', validators=[DataRequired()])
    students_fullname = StringField('Nama Lengkap', validators=[DataRequired()])
    students_gender = RadioField(choices = [('L', 'Laki-Laki'), ('P', 'Perempuan')])
    students_address = TextAreaField('Alamat', validators=[DataRequired()])
    submit_form = SubmitField('Kirim')

class InputViolation(FlaskForm):
    students_violation = TextAreaField('Pelanggaran', validators=[DataRequired()])
    submit_form_2 = SubmitField('Tambah')

nama = {1:'andi', 2:'bagas', 3:'cahyo', 4:'karin'}
nama_lengkap = {1:'andi firmansyah', 2:'bagas prasetyo', 3:'cahyo wibowo', 4:'karina dewi'}
alamat = {1:'pogung kidul', 2:'klebengan', 3:'prawirotaman', 4:'denggung'}
jk = {1:'L', 2:'L', 3:'L', 4:'P'}
pelanggaran = {1:['perang', 'tawuran'], 2:[], 3:[], 4:[]}

@app.route('/')
def home():
    return render_template('home.html', list_nama=nama)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<int:id>', methods=['GET', 'POST'])
def siswa(id):
    violation_form = InputViolation(csrf_enabled=False)
    if violation_form.validate_on_submit():
        pelanggaran[id].append(violation_form.students_violation.data)
    return render_template( 'siswa.html', 
                            fullname = nama_lengkap[id], 
                            address=alamat[id], 
                            sex=jk[id],
                            violation=pelanggaran[id],
                            template_form=violation_form
                            )

@app.route('/form', methods=['GET', 'POST'])
def form_page():
    students_form = InputStudents(csrf_enabled=False)
    if students_form.validate_on_submit():
        idn = int(len(nama)+1)
        nama[idn] = students_form.students_name.data
        nama_lengkap[idn] = students_form.students_fullname.data
        alamat[idn] = students_form.students_address.data
        jk[idn] = students_form.students_gender.data
        pelanggaran[idn] = []
    return render_template('form.html', 
                            template_form=students_form
                            )

if __name__ == '__main__':
    app.run(debug=True)