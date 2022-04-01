from sqlalchemy import text, engine_from_config
from config import config


engine = engine_from_config(config, prefix='db.')


def lista_sabores_ativos():
    with engine.connect() as con:
        statement = text("""SELECT nome, descricao, valor, link, ativo 
                            FROM sabores
                            WHERE ativo = 'SIM'""")
        rs = con.execute(statement)
        sabores = []
        item = rs.fetchone()
        while (item != None):
            sabores.append(dict(item))
            item = rs.fetchone()
    return sabores
