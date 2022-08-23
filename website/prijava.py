from flask import Blueprint, render_template

prijava = Blueprint('prijava', __name__)

@prijava.route('/prijava')
def login():
    return render_template("prijavi.html")

@prijava.route('/odjava')
def odjava():
    return "<p>Odjava</p>"

@prijava.route('/registriraj')
def registriraj():
    return render_template("registriraj.html")
