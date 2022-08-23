from flask import Blueprint, render_template

pogledi = Blueprint('pogledi', __name__)

@pogledi.route('/') #url za stranicu, gdje će se nalaziti
def home(): #funkcija

    return render_template ("pocetna.html")
