from flask import Blueprint, render_template, request, flash

prijava = Blueprint('prijava', __name__)

@prijava.route('/prijava', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("prijavi.html", boolean=True)

@prijava.route('/odjava')
def odjava():
    return "<p>Odjava</p>"

@prijava.route('/registriraj', methods=['GET', 'POST'])
def registriraj():
    if request.method == 'POST':
        email = request.form.get('email')
        ime = request.form.get('ime')
        sifra = request.form.get('sifra')
        sifra1 = request.form.get('sifra1')
    if len(email) < 4:
        flash('Email adresa je prekratka', category='error')
    elif len(ime)< 2:
        flash('Prvo ime mora biti veće od 1 znaka', category='error')
    elif sifra != sifra1:
        flash('Šifre se \ne podudaraju', category='error')
    elif len(password) < 7:
        flash('Šifra mora imati barem sedam znakova')
    else:
        flash('Račun je kreiran', category='succes')




    return render_template("registriraj.html")
