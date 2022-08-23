from flask import Flask

def create_app():
    app = Flask(__name__) #inicijalizacija flaska
    app.config['SECRET KEY'] = 'lozinkajelozinka'

    from .pogledi import pogledi #importam blueprint
    from .prijava import prijava

    app.register_blueprint(pogledi, url_prefix='/') #kako pristupam svakom url-u koji je u blueprintu
    app.register_blueprint(prijava, url_prefix='/')

    return app #aplikacija kreirana
