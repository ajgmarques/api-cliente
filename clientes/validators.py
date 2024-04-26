import re
from validate_docbr import CPF


def cpf_valido(numero_do_cpf):
    '''
    Verifica se o cpf é válido
    '''
    cpf = CPF()
    return cpf.validate(numero_do_cpf)


def nome_valido(nome):
    '''
    Verifica se o nome não contém números
    '''
    nome = nome.replace(' ', '')
    return nome.isalpha()


def rg_valido(rg):
    return len(rg) == 9


def celular_valido(celular):
    '''
    Verifica se o número de celular é válido (85 12345-6789)
    '''
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta
