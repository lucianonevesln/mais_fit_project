from datetime import datetime


def retorna_idade(data_nascimento):
    """
    Recebe uma data de nascimento em formato string, converte para data e
    calcula idade. Depois retona a idade como um valor inteiro.
    """
    nascimento = datetime.strptime(data_nascimento,'%Y-%m-%d' )
    ano_nascimento = nascimento.year
    data_atual = datetime.now()
    ano_atual = data_atual.year


    return ano_atual - ano_nascimento
