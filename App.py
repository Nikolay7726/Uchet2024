from select import select
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login.utils import _secret_key
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import False_
from sqlalchemy.ext import mypy
from sqlalchemy.testing import db
from DBclass import DBclass

app = Flask(__name__)
app.secret_key = 'Secret Key'
# Коннектимся к базе
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:coolerDEFe3@localhost/uchet_svt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Передаем объект приложения app в sqlalchemy
db = SQLAlchemy(app)
app.app_context().push()


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
    additionale = db.Column(db.String(100))

    def __init__(self, typesvt, otd, mol, inv, serial, namedomain, nameuser, typeos, additionale):
        self.typesvt = typesvt
        self.otd = otd
        self.mol = mol
        self.inv = inv
        self.serial = serial
        self.namedomain = namedomain
        self.nameuser = nameuser
        self.typeos = typeos
        self.additionale = additionale


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    passw = db.Column(db.Text, nullable=False)
    time = db.Column(db.Integer)

    def __init__(self, name, email, passw, time):
        self.name = name
        self.email = email
        self.passw = passw
        self.time = time


@app.route('/home')
def index():
    all_svt = SVT.query.all()
    return render_template("index.html", employees=all_svt)


@app.route('/')
def login():
    return render_template('login.html')


@app.route("/registration", methods=["POST", "GET"])
def registration():
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 \
                and len(request.form['passwd']) > 4 and request.form['passwd']:
                 hash = generate_password_hash(request.form['passwd'])
            res = db.

    return render_template('registration.html')


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
        additionale = request.form['additionale']

        my_svt = SVT(typesvt, otd, mol, inv, serial, namedomain, nameuser, typeos, additionale)
        db.session.add(my_svt)
        db.session.commit()

        flash("Запись успешно добавлена")

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
        my_svt.additionale = request.args.getlist('additionale[]')
        # my_svt.additionale = request.form['additionale']

        db.session.commit()
        flash("Запись успешно обновлена")

        return redirect(url_for('index'))


@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_svt = SVT.query.get(id)
    db.session.delete(my_svt)
    db.session.commit()
    flash("Запись удалена")
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
