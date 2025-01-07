from cryptography.fernet import Fernet
from flask import Flask

app = Flask(__name__)

# Génération de la clé de chiffrement et création de l'objet Fernet
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/exercice1')
def hello_world():
    return "Bienvenue sur mon site html 1"

@app.route('/exercice2')
def hello_world():
    return "Bienvenue sur mon site html 2"

@app.route('/exerciceX')
def hello_world():
    return "Bienvenue sur mon site html X"

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
