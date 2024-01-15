from flask import Flask, g
import time, math, psycopg2

import sqlalchemy.sql.selectable
from sqlalchemy.dialects import postgresql


def connect_db():
    conn = psycopg2.connect(dbname="uchet_svt", user="admin", password="coolerDEFe3", host="127.0.0.1")
    print("Подключение установлено")
    return conn


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


class DBclass:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


def addUser(self, name, email, hpasswd):
    try:
        self.__cur.execute(f"SELECT COUNT() as 'count' FROM user WHERE email LIKE '{email}'")
        res = self.__cur.fetchone()
        if res['count'] > 0:
            print("Пользователь с таким email уже существует")
            return False
        tm = math.floor(time.time())
        self.__cur.execute("INSERT INTO user VALUES(NULL, ?, ?, ?, ?)", (name, email, hpasswd, tm))
        self.__db.commit()
    except psycopg2.OperationalError as ex:
        print("Ошибка" + str(ex))
        return False

    return True
