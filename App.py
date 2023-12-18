from select import select
from flask import Flask, render_template, request, redirect, url_for
from flask_login.utils import _secret_key
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import False_
from sqlalchemy.testing import db

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


    def __init__(self, typesvt, otd, mol, inv):
        self.typesvt = typesvt
        self.otd = otd
        self.mol = mol
        self.inv = inv


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        typesvt = request.form['typesvt']
        otd = request.form['otd']
        mol = request.form['mol']
        inv = request.form['inv']

        my_svt = SVT (typesvt, otd, mol, inv)
        db.session.add(my_svt)
        db.session.commit()
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
