from flask import Flask, render_template, session, redirect
import os
from questions import questions
from resultats import resultats 

# Création de l'application
app = Flask(__name__)
#création d"une clée secrete
app.secret_key = os.urandom(24)


# route de l'accueil
@app.route('/')
def index():
    session["numero_question"] = 0
    session["score"] = {"Le Fraggeur Fou 🎯": 0, "Le Loup Solitaire 🐺": 0, "Le Cerveau Stratégique 🧠": 0, "Le Contrôleur Tactique 🛡️": 0}
    return render_template("index.html")

# route de la page 2
@app.route('/question')
def page2():
    global questions
    nb_question = session["numero_question"]
    if nb_question < len(questions) :
        ennonce_question = questions[nb_question]["ennonce"]
        questions_copy = questions[nb_question].copy()
        questions_copy.pop("ennonce")
        reponses = list(questions_copy.values())
        session["clefs"] = list(questions_copy.keys())
        return render_template("question.html", question = ennonce_question, reponses = reponses)

    else :
        global resultats
        score = sorted(session["score"], key=session["score"].get , reverse = True)
        vainqueur = score[0]
        description = resultats[vainqueur]
        return render_template("resultat.html", vainqueur = vainqueur, description = description)

# route de la page 3
@app.route("/reponse/<numero>")
def reponse(numero):
    session["numero_question"] += 1
    resultat = session["clefs"][int(numero)]
    session["score"][resultat] += 1
    return redirect("/question")






# Exécution du code
app.run(host='0.0.0.0', port=81)