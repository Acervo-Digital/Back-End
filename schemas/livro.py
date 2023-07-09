from pydantic import BaseModel
from typing import List, Optional
from model.livro import Livro

from schemas import AvaliacaoSchema


class LivroSchema(BaseModel):
    """ Define como um novo livro deve ser representado
    """
    nome: str = "Romeu e Julieta"
    genero: str = "Romance"
    quantidade: Optional[int] = 12
    valor: float = 22.50


class LivroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do livro.
    """
    nome: str = "Teste"


class ListagemLivrosSchema(BaseModel):
    """ Define como uma listagem de livros será retornada.
    """
    livros:List[LivroSchema]


def apresenta_livros(livros: List[Livro]):
    """ Retorna uma representação do livro seguindo o schema definido em
        LivroViewSchema.
    """
    result = []
    for livro in livros:
        result.append({
            "nome": livro.nome,
            "genero": livro.genero,
            "quantidade": livro.quantidade,
            "valor": livro.valor,
        })

    return {"livros": result}


class LivroViewSchema(BaseModel):
    """ Define como um livro será retornado: livro + avaliação.
    """
    id: int = 1
    nome: str = "Romeu e Julieta"
    genero: str = "Romance"
    quantidade: Optional[int] = 12
    valor: float = 22.50
    total_avaliacoes: int = 1
    avaliacoes:List[AvaliacaoSchema]


class LivroDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome: str

def apresenta_livro(livro: Livro):
    """ Retorna uma representação do livro seguindo o schema definido em
        LivroViewSchema.
    """
    return {
        "id": livro.id,
        "nome": livro.nome,
        "genero": livro.genero,
        "quantidade": livro.quantidade,
        "valor": livro.valor,
        "total_avaliacoes": len(livro.avaliacoes),
        "avaliacoes": [{"nota": c.nota} for c in livro.avaliacoes]
    }
