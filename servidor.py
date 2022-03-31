from flask import Flask, request
from database import *

app = Flask(__name__)


@app.route("/")
def home():
    return "Home!"

@app.route("/lista")
def listar_sabores():
    sabores = {}
    sabores["sabores"] = lista_sabores_ativos()
    return sabores

@app.route("/clientes", methods=['POST'])
def cadastra_cliente():
    dados_cliente = request.json
    cadastrar_cliente(dados_cliente)
    return {}

if __name__ == "__main__":
    app.run("localhost", port=5000, debug=True)
#     app.run()
