# Baixando as ferramentas necessarias
from flask          import Flask, request, render_template, jsonify
from flaskext.mysql import MySQL


# Acionando ferramenta de contato com o banco de dados
mysql = MySQL()

# Ferramenta que vai permitir acionar o servidor 
app = Flask(__name__)

# Script para conexao com o banco de dados
app.config['MYSQL_DATABASE_USER']     = 'b41b536da2d233'
app.config['MYSQL_DATABASE_PASSWORD'] = 'a2d3d9bb'
app.config['MYSQL_DATABASE_DB']       = 'heroku_f7de65fdae1ab14'
app.config['MYSQL_DATABASE_HOST']     = 'us-cdbr-east-05.cleardb.net'

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
    nomes = cursor.fetchall()
    conn.commit()
    teste = {}
    teste["nomes"] = nomes
    return teste
    cursor.close()
    conn.close()


# Scrip que define a localidade onde o servidor sera executado
# if __name__ == '__main__':
#     app.run(host = 'localhost', port = 5002, debug = True)