from config import *
from model import *
from flask import Flask

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/listar_comidas")
def listar_comidas():
    with db_session:
        comidas = Comida.select() 
        return render_template("listar_comidas.html", comidas=comidas)

@app.route("/form_adicionar_comida")
def form_adicionar_comida():
    return render_template("form_adicionar_comida.html")

@app.route("/adicionar_comida")
def adicionar_comida():

    nome=request.args.get("nome")
    marca=request.args.get("marca")
    valor=request.args.get("valor")
    validade=request.args.get("validade")
    with db_session:
        c=Comida(**request.args)
        commit()
        return redirect("listar_comidas") 
