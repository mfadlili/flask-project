from flask import Flask, render_template, requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired 


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

nama = {1:'andi', 2:'bagas', 3:'cahyo', 4:'karin'}
nama_lengkap = {1:'andi firmansyah', 2:'bagas prasetyo', 3:'cahyo wibowo', 4:'karina dewi'}
alamat = {1:'pogung kidul', 2:'klebengan', 3:'prawirotaman', 4:'denggung'}
jk = {1:'L', 2:'L', 3:'L', 4:'P'}

@app.route('/')
def home():
    return render_template('home.html', list_nama=nama)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<int:id>')
def siswa(id):
    return render_template('siswa.html', fullname = nama_lengkap[id], address=alamat[id], sex=jk[id])

@app.route('/form')
def form_page():
    return

if __name__ == '__main__':
    app.run(debug=True)