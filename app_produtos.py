from sqlalchemy import Engine, select
from sqlalchemy.orm import Session
from decimal import *

from app_categorias import selecionar_categoria
from models import Produto


def listar(engine: Engine):
    with Session(engine) as session:
        stmt = select(Produto).order_by(Produto.nome)
        produtos = session.execute(stmt).scalars()
        print("Nome, preco, estoque, ativo, nome da categoia, Data cadastro, Data de modificacao")
        for produto in produtos:
            print(f"{produto.nome}, {produto.preco}, {produto.estoque},"
                  f"{"Ativo" if produto.ativo else "Inativo"}, {produto.categoria.nome}, "
                  f"{produto.dta_cadastro}, {produto.data_atualizacao}")

def adicionar (engine:Engine):
    with Session(engine) as session:
        p = Produto()
        p.nome = input("Qual o nome do produto? ")
        p.preco = Decimal(input("Qual o preço do produto? R$"))
        p.estoque = int(input("Qual o estoque inicial do produto? "))
        x= input("O produto esta ativo? (s/n) ").lower()
        p.ativo = True if x[0] == 's' else False
        print("Selecione a categoria do produto")
        p.categoria = selecionar_categoria(session)
        session.add(p)
        try:
            session.commit()
        except:
            print("Erro na inserção do produto")
        else:
            print("produto incluido com sucesso")