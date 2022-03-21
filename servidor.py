# Baixando as ferramentas necessarias
import re
from flask          import Flask, request, render_template, jsonify
from flaskext.mysql import MySQL
import json


# Acionando ferramenta de contato com o banco de dados
mysql = MySQL()

# Ferramenta que vai permitir acionar o servidor 
app = Flask(__name__)

# Script para conexao com o banco de dados
app.config['MYSQL_DATABASE_USER']     = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB']       = ''
app.config['MYSQL_DATABASE_HOST']     = ''

# Iniciando a conexao com o banco de dados
mysql.init_app(app)


# Criando rota para renderizar o front-end
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Retorna todos os nomes armazenados em banco de dados
@app.route('/lista', methods=['GET', 'POST'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select id, nome, descricao, link, ativo from sabores')
    rv = cursor.fetchall()
    payload = []
    content = {}
    for result in rv:
        content = {"id": result[0], "nome": result[1],"descricao": result[2], "link": result[3], "ativo": result[4]}
        payload.append(content)
        content = {}
    return jsonify(payload)


# Scrip que define a localidade onde o servidor sera executado
if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)