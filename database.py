from sqlalchemy import text, engine_from_config, Integer
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
    with engine.connect() as con:
        statement = text("""SELECT nome_completo, cpf, nascimento, genero, celular, cep, logradouro, numero, complemento, bairro, email, senha 
                            FROM clientes
                            WHERE ativo = 1""")
        rs = con.execute(statement)
        clientes = []
        item = rs.fetchone()
        while (item != None):
            clientes.append(dict(item))
            item = rs.fetchone()
    return clientes


def cliente_existe(cpf):
    with engine.connect() as con:
        statement = text("""SELECT cpf 
                            FROM clientes
                            WHERE cpf = :cpf""")
        rs = con.execute(statement, cpf=cpf)
        item = rs.fetchone()
        if item:
            return "cliente existe"


# if __name__ == "__main__":
#     print(cliente_existe("11111111111"))