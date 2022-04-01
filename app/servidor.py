from flask import Flask, request, jsonify
from database import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Home!"

@app.route("/lista")
def listar_sabores():
    return jsonify(lista_sabores_ativos())

@app.route("/clientes", methods=['POST'])
def cadastra_cliente():
    dados_cliente = request.json
    cadastrar_cliente(dados_cliente)
    return {}

@app.route("/clientes", methods=['GET'])
def lista_cliente():
    return jsonify(listar_clientes())

@app.route("/cliente-existe/<cpf>")
def verifica_cliente(cpf):
    return cliente_existe(cpf)



# if __name__ == "__main__":
#     app.run("localhost", port=5000, debug=True)
