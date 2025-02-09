from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

# Génération de la clé de chiffrement et création de l'objet Fernet
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def Hello_World():
    return f"Hello world !"
    
@app.route('/exercice1')
def Exo1():
    return render_template('exercice1.html')
    
@app.route('/exercice2')
def Exo2():
    return render_template('exercice2.html')

@app.route('/exerciceX')
def ExoX():
    return render_template('exerciceX.html')

@app.route('/actualite')
def Actu():
    return render_template('actualite.html')

@app.route('/svg')
def svg():
    return render_template('svg.html')

@app.route('/maison')
def maison():
    return render_template('maison.html')

@app.route('/jack')
def jack():
    return render_template('jack.html')

@app.route('/chenille')
def chenille():
    return render_template('chenille.html')

@app.route('/jeudesbase')
def jeu():
    return render_template('Jeu_Des_Base.html')

@app.route('/outiljava')
def js():
    return render_template('Outils_JS.html')

@app.route('/rouletterusse')
def roulette():
    return render_template('Roulette_Russe_Etape_1_Barillet_Vide.html')

    
@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

# Exercice 1 : Route pour décryptage
@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_bytes = token.encode()  # Conversion str -> bytes
        valeur_decryptee = f.decrypt(token_bytes)  # Décryptage du token
        return f"Valeur décryptée : {valeur_decryptee.decode()}"  # Retourne la valeur décryptée en str
    except Exception as e:
        return f"Erreur lors du décryptage : {e}"

if __name__ == "__main__":
    app.run(debug=True)
