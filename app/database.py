from sqlalchemy import text, engine_from_config
from config import config
import jwt


engine = engine_from_config(config, prefix='db.')


def lista_sabores_ativos():
    with engine.connect() as con:
        statement = text("""SELECT nome, descricao, link, ativo 
                            FROM sabores
                            WHERE ativo = 1""")
        rs = con.execute(statement)
        sabores = []
        item = rs.fetchone()
        while (item != None):
            sabores.append(dict(item))
            item = rs.fetchone()
    return sabores

def cadastrar_cliente(dados):
    nome_completo = dados["nome_completo"]
    cpf = dados["cpf"]
    nascimento = dados["nascimento"]
    genero = dados["genero"]
    celular = dados["celular"]
    cep = dados["cep"]
    logradouro = dados["logradouro"]
    numero = dados["numero"]
    complemento = dados["complemento"]
    bairro = dados["bairro"]
    email = dados["email"]
    senha = dados["senha"]
    senha = jwt.encode({"senha":"{0}".format(senha)}, "secret", algorithm="HS256")
    with engine.connect() as con:
        statement = text("""INSERT INTO clientes 
            (   nome_completo, cpf, nascimento, genero, celular, cep, logradouro, numero, 
                complemento, bairro, email, senha ) values
            (:nome_completo, :cpf, :nascimento, :genero, :celular, :cep, :logradouro, 
            :numero, :complemento, :bairro, :email, :senha)
        """)
        con.execute(statement, nome_completo=nome_completo, cpf=cpf, 
                    nascimento=nascimento, genero=genero, celular=celular, cep=cep, 
                    logradouro=logradouro, numero=numero, 
                    complemento=complemento, bairro=bairro, email=email, senha=senha)

def listar_clientes():
    """
        Lista todos os clientes da base de dados baseado em filtros
    """
    #TODO -> precisamos implementar os filtros de buscas
    with engine.connect() as con:
        statement = text("""SELECT nome_completo, cpf, nascimento, genero, celular, cep, logradouro, numero, complemento, bairro, email, senha 
                            FROM clientes"""
                            )
        rs = con.execute(statement)
        clientes = []
        item = rs.fetchone()
        while (item != None):
            clientes.append(dict(item))
            item = rs.fetchone()
    return clientes


def cpf_existe(cpf):
    """
        Verifica se já existe um cpf cadastrado no banco
    """
    with engine.connect() as con:
        statement = text("""SELECT cpf 
                            FROM clientes
                            WHERE cpf = :cpf""")
        rs = con.execute(statement, cpf=cpf)
        item = rs.fetchone()
        if item:
            return True
        else:
            return False

def email_existe(email):
    """
        Verifica se já existe um e-mail cadastrado no banco
    """
    with engine.connect() as con:
        statement = text("""SELECT email 
                            FROM clientes
                            WHERE email = :email""")
        rs = con.execute(statement, email=email)
        item = rs.fetchone()
        if item:
            return True
        else:
            return False
