from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash

from Uchet import app, db
from Uchet.models import User, SVT

@app.route('/main')
def index():
    all_svt = SVT.query.all()
    return render_template("index.html", employees=all_svt)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('passw')

    if login and password:
        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.passw, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Логин или пароль введены некорректно')
    else:
        flash('Пожалуйста введите свои данные')
    return render_template('login.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    FIO = request.form.get('FIO')
    login = request.form.get('login')
    password = request.form.get('passw')
    password2 = request.form.get('passw2')
    # time = request.form.get('time')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Пожалуйста не бейте')
        elif password != password2:
            flash('Пароли не совпадают')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = User(FIO=FIO, login=login, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login_page'))
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
