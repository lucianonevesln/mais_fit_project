from sqlalchemy import text, engine_from_config
from config import config
import jwt


engine = engine_from_config(config, prefix='db.')


def lista_sabores_ativos():
    with engine.connect() as con:
        statement = text("""SELECT nome, descricao, link, ativo 
                            FROM marmitas
                            WHERE ativo = 1""")
        rs = con.execute(statement)
        sabores = []
        item = rs.fetchone()
        while (item != None):
            sabores.append(dict(item))
            item = rs.fetchone()
    return sabores

def lista_kits_ativos():
    with engine.connect() as con:
        statement = text("""SELECT id, descricao, qtd_max_marmitas, valor, ativo
                            FROM kits
                            WHERE ativo = 1""")
        rs = con.execute(statement)
        kits = []
        item = rs.fetchone()
        while (item != None):
            kits.append(dict(item))
            item = rs.fetchone()
    return kits


def lista_pagamentos_ativo():
    with engine.connect() as con:
        statement = text("""SELECT id, descricao, link 
                            FROM meios_pagamentos
                            WHERE ativo = 1""")
        rs = con.execute(statement)
        pagamento = []
        item = rs.fetchone()
        while (item != None):
            pagamento.append(dict(item))
            item = rs.fetchone()
    return pagamento

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

def inserir_pedido(cliente_id, formas_pagamento, itens_pedido):

    data_emissao = datetime.now()
    
    with engine.connect() as con:
        try:
            # inserindo pedido
            statement = text ("""INSERT INTO pedidos 
                                (status, data_emissao, cliente_id)
                                VALUES (:status, :data_emissao, :cliente_id)""")

            con.execute(statement, status="iniciado", data_emissao=data_emissao,
                        cliente_id=cliente_id)

            pedido_id = retorna_id_ultimo_pedido()
            # após inserir o pedido, vou inserir as formas de pagamento do pedido
            inserir_formas_pagamento(formas_pagamento, pedido_id)
            # após, devemos inserir os itens do pedido
            inserir_itens_pedido(itens_pedido, pedido_id)

            return pedido_id
        except Exception:
            return None


def retorna_id_ultimo_pedido():
    with engine.connect() as con:
        statement = text (
            """
                SELECT MAX(id) as maxId FROM pedidos
            """
        )
        rs = con.execute(statement)
        pedido_id = rs.fetchone()

    return pedido_id[0]


def inserir_formas_pagamento(formas_pagamento, pedido_id):
    with engine.connect() as con:
        for meios_pagamento in formas_pagamento:
            statement = text (
                """
                    INSERT INTO formas_pagamentos (qtd, meio_pagamento_id, pedido_id)
                    VALUES (:qtd, :meio_pagamento_id, :pedido_id)
                """
            )
            con.execute(statement, qtd=meios_pagamento['qtd_pagamento'], 
                        meio_pagamento_id=meios_pagamento['meio_pagamento_id'], 
                        pedido_id=pedido_id)


def inserir_itens_pedido(itens_pedido, pedido_id):
    with engine.connect() as con:
        for kit in itens_pedido:
            statement = text (
                """
                    INSERT INTO itens_pedidos (preco, pedido_id, kit_id)
                    VALUES (:preco, :pedido_id, :kit_id)
                """
            )

            preco = buscar_preco_kit(kit['kit_id'])

            con.execute(statement, preco=preco, pedido_id=pedido_id,
                        kit_id=kit['kit_id'])

            for marmita in kit["marmitas"]:
                statement = text (
                    """
                        INSERT INTO itens_kits (qtd_marmita, marmita_id, item_pedido_id)
                        VALUES (:qtd_marmita, :marmita_id, :item_pedido_id)
                    """
                )
                item_pedido_id = retorna_id_item_pedido(pedido_id)
                con.execute(statement, qtd_marmita=marmita["qtd_marmita"],
                            marmita_id=marmita['marmita_id'],
                            item_pedido_id=item_pedido_id)


def buscar_preco_kit(kit_id):
    with engine.connect() as con:
        statement = text("""SELECT valor FROM kits WHERE id = :kit_id""")
        rs = con.execute(statement, kit_id=kit_id)
        preco = rs.fetchone()
    return preco[0]

def retorna_id_item_pedido(pedido_id):
    with engine.connect() as con:
        statement = text("""SELECT MAX(id) as maxId 
                            FROM itens_pedidos
                            WHERE pedido_id = :pedido_id""")
        rs = con.execute(statement, pedido_id=pedido_id)
        item_pedido_id = rs.fetchone()
    return item_pedido_id[0]