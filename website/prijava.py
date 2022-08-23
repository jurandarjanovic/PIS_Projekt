from flask import Blueprint

prijava = Blueprint('prijava', __name__)

@prijava.route('/prijava')
def login():
    return "<p>Prijava</p>"

@prijava.route('/odjava')
def odjava():
    return "<p>Odjava</p>"

@prijava.route('/registriraj')
def registriraj():
    return "<p>Registriraj</p>"
