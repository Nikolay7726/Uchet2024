from flask_login import UserMixin
from sqlalchemy import UniqueConstraint

from Uchet import db, manager


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


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    FIO = db.Column(db.Text, nullable=False)
    login = db.Column(db.String(128), nullable=False, unique=True)
    passw = db.Column(db.String(128), nullable=False)
    passw2 = db.Column(db.String(128), nullable=False)
    time = db.Column(db.Date)

    # def __init__(self, FIO, login, passw, passw2, time):
    #     self.FIO = FIO
    #     self.login = login
    #     self.passw = passw
    #     self.passw2 = passw2
    #     self.time = time


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
