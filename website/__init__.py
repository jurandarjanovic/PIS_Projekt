from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #inicijalizacija flaska
    app.config['SECRET KEY'] = 'lozinkajelozinka'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #ovdje se nalazi baza
    db.init_app(app)
    
    from .pogledi import pogledi #importam blueprint
    from .prijava import prijava

    app.register_blueprint(pogledi, url_prefix='/') #kako pristupam svakom url-u koji je u blueprintu
    app.register_blueprint(prijava, url_prefix='/')

    return app #aplikacija kreirana
