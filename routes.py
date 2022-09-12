from flask import render_template, url_for, redirect, flash, request
from app import app, db
from models import Students, Violation, User
from form import InputStudents, InputViolation, DeleteStudents, LoginUser, RegisterUser
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def home():
    students = Students.query.all()
    lst_nama = {}
    for student in students:
        lst_nama[student.id] = student.name
    return render_template('home.html', list_nama=lst_nama,)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<int:id>', methods=['GET', 'POST'])
def siswa(id):

    stud_by_id = Students.query.get(id)
    nama = stud_by_id.name
    nama_lengkap = stud_by_id.full_name
    alamat = stud_by_id.address
    jk = stud_by_id.gender
    pelanggaran = Violation.query.filter_by(student_id=id).all()
    pelanggaran_list = dict()
    point = 0
    for v in pelanggaran:
        pelanggaran_list[v.id] = v.violation
        point += v.point

    violation_form = InputViolation(csrf_enabled=False)

    if violation_form.validate_on_submit():

        violation_input = violation_form.students_violation.data
        point_input = violation_form.setudent_add_point.data
        violation1 = Violation(violation_input, id, point_input)
        db.session.add(violation1)
        db.session.commit() 

        return redirect(url_for('siswa', id=id))

    return render_template( 'siswa.html',
                            name = nama,
                            fullname = nama_lengkap, 
                            address=alamat, 
                            sex=jk,
                            violation=pelanggaran_list,
                            template_form=violation_form,
                            point_student = point)


@app.route('/form', methods=['GET', 'POST'])
@login_required
def form_page():
    students_form = InputStudents(csrf_enabled=False)
    if students_form.validate_on_submit():
        nama = students_form.students_name.data
        nama_lengkap = students_form.students_fullname.data
        alamat = students_form.students_address.data
        jk = students_form.students_gender.data

        std = Students(nama, nama_lengkap, alamat, jk)
        db.session.add(std)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('form.html', 
                            template_form=students_form
                            )

@app.route('/delete_students', methods=['GET', 'POST'])
@login_required
def delete():
    delete_form = DeleteStudents(csrf_enabled=False)
    if delete_form.validate_on_submit():

        id = delete_form.id_delete.data
        id_del = Students.query.get(id)
        vio_del = Violation.query.filter_by(student_id=id).all()
        for violation in vio_del:
            db.session.delete(violation)
        db.session.delete(id_del)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('delete.html',
                            template_form = delete_form,
                            )

@app.route('/delete_violation/<int:id>')
@login_required
def delete_violation(id):
    del_vio = Violation.query.get(id)
    stud_id = del_vio.student_id
    db.session.delete(del_vio)
    db.session.commit()
    return redirect(url_for('siswa', id=stud_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginUser()
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        password = form.password.data
        user_in = User.query.filter_by(username=form.username.data).first()

        if user_in is None or user_in.check_password(form.password.data) is False:
            flash('Username or Password incorrect')
            return redirect(url_for('login'))

        login_user(user_in)
        flash('Success')
        next = request.args.get('next')
        if next==None or next[0]!='/':
            next = url_for('home')

        return redirect(next)
    
    return render_template('login.html', template_form=form)

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegisterUser()
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()
        flash('Thank you for registering your account!')
        return redirect(url_for('login'))
    
    return render_template('register.html', template_form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out.')
    return redirect(url_for('home'))

@app.errorhandler(404)
def error_404(error):
    return render_template('error.html'), 404

@app.errorhandler(AttributeError)
def error(error):
    return render_template('error.html')
