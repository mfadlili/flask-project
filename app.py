from flask import Flask, render_template, request
from form import InputStudents, InputViolation
from connect_db import connect_mysql_db

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"


@app.route('/')
def home():
    try:
        db = connect_mysql_db()
        lst_nama = db.query_nama()
        nama = {}
        for i in range(len(lst_nama)):
            nama[i+1] = lst_nama[i]
        db.close_db()
    except:
        print('error')
    return render_template('home.html', list_nama=nama,)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<int:id>', methods=['GET', 'POST'])
def siswa(id):
    try:
        db = connect_mysql_db()
        data = db.query_data_siswa(id)
        pelanggaran = db.query_pelanggaran(id)
        nama_lengkap = data[1]
        alamat = data[2]
        jk = data[3]
        db.close_db()
    except:
        print('error')

    violation_form = InputViolation(csrf_enabled=False)

    if violation_form.validate_on_submit():
        violation_input = violation_form.students_violation.data
        try:
            db = connect_mysql_db()
            db.input_pelanggaran_siswa(id, violation_input)
            db.close_db()
        except:
            print('error')

    return render_template( 'siswa.html', 
                            fullname = nama_lengkap, 
                            address=alamat, 
                            sex=jk,
                            violation=pelanggaran,
                            template_form=violation_form,
                            )


@app.route('/form', methods=['GET', 'POST'])
def form_page():
    students_form = InputStudents(csrf_enabled=False)
    if students_form.validate_on_submit():
        nama = students_form.students_name.data
        nama_lengkap = students_form.students_fullname.data
        alamat = students_form.students_address.data
        jk = students_form.students_gender.data
        try:
            db = connect_mysql_db()
            db.input_data_siswa(nama, nama_lengkap, alamat, jk)
            db.close()
        except:
            print('error')
    return render_template('form.html', 
                            template_form=students_form
                            )

if __name__ == '__main__':
    app.run(debug=True)