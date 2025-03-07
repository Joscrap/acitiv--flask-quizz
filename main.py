from flask import Flask, render_template, session, redirect
import os
from questions import questions
from resultats import resultats

# Création de l'application
app = Flask(__name__)
#création d"une clée secrete
app.secret_key = os.urandom(24)


# Exécution du code
app.run(host='0.0.0.0', port=81)