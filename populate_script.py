import os
import django
import random

from validate_docbr import CPF
from faker import Faker

from setup import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()


from clientes.models import Cliente  # tem de estar imediatamente antes da função

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt-BR')
    Faker.seed(20)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(), fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = '{}{}{}{}'.format(random.randrange(10, 21),
                               random.randrange(100, 999),
                               random.randrange(100, 999),
                               random.randrange(0, 9))
        celular = '{} 9{}-{}'.format(random.randrange(10, 99),
                                     random.randrange(4000, 9999),
                                     random.randrange(4000, 9999))
        ativo = random.choice([True, False])
        p = Cliente(nome=nome, email=email, cpf=cpf,
                    rg=rg, celular=celular, ativo=ativo)
        p.save()


criando_pessoas(50)
print('Sucesso...')
