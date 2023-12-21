from select import select
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login.utils import _secret_key
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import False_
from sqlalchemy.ext import mypy
from sqlalchemy.testing import db

app = Flask(__name__)
app.secret_key = 'Secret Key'
# Коннектимся к базе
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:coolerDEFe3@localhost/uchet_svt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Передаем объект приложения app в sqlalchemy
db = SQLAlchemy(app)
app.app_context().push()


# @app.route('/create', methods=['GET', 'POST'])
# def create():
#     if request.method == 'GET':
#         return render_template('create.html')
#
#
# app.run(host='localhost', port=5000)

class SVT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typesvt = db.Column(db.String(100))
    otd = db.Column(db.String(100))
    mol = db.Column(db.String(100))
    inv = db.Column(db.String(100))
    serial = db.Column(db.String(100))
    namedomain = db.Column(db.String(100))
    nameuser = db.Column(db.String(100))
    typeos = db.Column(db.String(100))

    def __init__(self, typesvt, otd, mol, inv, serial, namedomain, nameuser, typeos):
        self.typesvt = typesvt
        self.otd = otd
        self.mol = mol
        self.inv = inv
        self.serial = serial
        self.namedomain = namedomain
        self.nameuser = nameuser
        self.typeos = typeos


@app.route('/')
def index():
    all_svt = SVT.query.all()
    return render_template("index.html", employees=all_svt)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        typesvt = request.form['typesvt']
        otd = request.form['otd']
        mol = request.form['mol']
        inv = request.form['inv']
        serial = request.form['serial']
        namedomain = request.form['namedomain']
        nameuser = request.form['nameuser']
        typeos = request.form['typeos']

        my_svt = SVT (typesvt, otd, mol, inv, serial, namedomain, nameuser, typeos)
        db.session.add(my_svt)
        db.session.commit()

        return redirect(url_for('index'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_svt = SVT.query.get(request.form.get('id'))

        my_svt.typesvt = request.form['typesvt']
        my_svt.otd = request.form['otd']
        my_svt.mol = request.form['mol']
        my_svt.inv = request.form['inv']
        my_svt.serial = request.form['serial']
        my_svt.namedomain = request.form['namedomain']
        my_svt.nameuser = request.form['nameuser']
        my_svt.typeos = request.form['typeos']

        db.session.commit()
        flash("Запись успешно обновлена")

        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
