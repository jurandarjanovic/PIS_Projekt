from flask import Blueprint

pogledi = Blueprint('pogledi', __name__)

@pogledi.route('/') #url za stranicu, gdje će se nalaziti
def home(): #funkcija
    return "<h1> Dobro došli! </h1>"
