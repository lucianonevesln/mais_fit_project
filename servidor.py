# Baixando as ferramentas necessarias
from flask          import Flask, request, render_template, jsonify
from flaskext.mysql import MySQL

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

# Estrutura para inserir informacao no banco de dados via aplicacao web
@app.route('/login', methods=['POST'])
def cadastrar_informacao():

    # recebendo inputs do form html
    nome  = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    # armazenando informacao no banco de dados
    if nome and email and senha:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute( # insere o usuario em banco de dados
            'insert into cadastro (nome, email, senha) values (%s, %s, %s);', 
            (nome, email, senha)
            )
        conn.commit()
        return render_template('index.html')

    # desconecta do bando de dados e do cursor
    cursor.close()
    conn.close()

# Retorna todos os nomes armazenados em banco de dados
@app.route('/lista', methods=['GET', 'POST'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select nome from sabores') # retorna uma consulta em banco de dados
    nomes = cursor.fetchall()
    conn.commit()
    teste = {}
    teste["nomes"] = nomes
    return teste
    cursor.close()
    conn.close()

# Scrip que define a localidade onde o servidor sera executado
if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)