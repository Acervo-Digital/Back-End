from pydantic import BaseModel


class AvaliacaoSchema(BaseModel):
    """ Define como um novo avaliacao a ser inserido deve ser representado
    """
    livro_id: int = 1
    nota: float = 9.5
