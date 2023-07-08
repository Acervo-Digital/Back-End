from sqlalchemy import Column, Float, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from model import Base

class Avaliacao(Base):
    __tablename__ = 'avaliacao'

    id = Column(Integer, primary_key=True)
    nota = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o avaliacao e um livro.
    # Aqui está sendo definido a coluna 'livro' que vai guardar
    # a referencia ao livro, a chave estrangeira que relaciona
    # um livro ao avaliacao.
    livro = Column(Integer, ForeignKey("livro.pk_livro"), nullable=False)

    def __init__(self, nota:float, data_insercao:Union[DateTime, None] = None):
        """
        Cria uma avaliacao

        Arguments:
            nota: a nota passada.
            data_insercao: data de quando a nota foi feito ou inserido
                           à base
        """
        self.nota = nota
        if data_insercao:
               self.data_insercao = data_insercao
