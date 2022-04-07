from flask import Flask, request, jsonify
from flask_cors import CORS

from database import *
from helpers import retorna_idade


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Olá, você está na API da mais-fit!"

@app.route("/lista")
def listar_sabores():
    return jsonify(lista_sabores_ativos()), 200

@app.route("/formapagamento")
def listar_pagamentos():
    return jsonify(lista_pagamentos_ativo())


@app.route("/clientes", methods=['POST'])
def cadastra_cliente():
    dados_cliente = request.json

    idade = retorna_idade(dados_cliente['nascimento'])
    cpf_exists = cpf_existe(dados_cliente['cpf'])
    email_exists = email_existe(dados_cliente['email'])

    if cpf_exists:
        return {"message": "Ja existe um cliente com esse CPF"}, 400
    if idade < 10:
        return {"message": "Este cliente possui idade menor que 10 anos"}, 400
    if email_exists:
        return {"message": "Ja existe um cliente com esse e-mail"}, 400

    try:
        cadastrar_cliente(dados_cliente)
    except:
        return {"message": "Nao foi possivel cadastrar o cliente."}, 500

    return {"message": "Cliente cadastrado com sucesso!"}, 200


@app.route("/clientes", methods=['GET'])
def lista_cliente():
    return jsonify(listar_clientes()), 200


@app.route("/verifica-cpf/<cpf>")
def verifica_cpf(cpf):
    cpf_exists = cpf_existe(cpf)
    if cpf_exists:
        return {"message": "Ja existe um cliente com esse CPF "}, 200
    return {"message": "Nao existe um cliente com esse CPF "}, 400


@app.route("/verifica-email/<email>")
def veirfica_email(email):
    email_exists = email_existe(email)
    if email_exists:
        return {"message": "Ja existe um cliente com esse E-mail"}, 200
    return {"message": "Nao existe um cliente com esse E-mail"}, 400

# lembrar de comentar essa parte quando for subir para o heroku
if __name__ == "__main__":
    app.run("localhost", port=5000, debug=True)
