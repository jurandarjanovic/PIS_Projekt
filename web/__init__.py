from flask import Flask

def create_app():
    app = Flask(__name__) #inicijalizacija flaska
    app.config['SECRET KEY'] = 'lozinkajelozinka'

    return app #aplikacija kreirana
