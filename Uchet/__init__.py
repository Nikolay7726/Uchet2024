import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app: Flask = Flask(__name__)
app.secret_key = 'Secret Key'
# Коннектимся к базе
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:coolerDEFe3@localhost/uchet_svt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Передаем объект приложения app в sqlalchemy
db = SQLAlchemy(app)
app.app_context().push()
manager = LoginManager(app)





from Uchet import models, routes, DBclass
