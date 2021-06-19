
from .persistencia import Persistencia


class Agenda:

    def __init__(self) -> None:

        self.persistencia = Persistencia()

        self.dict = self.persistencia.contact_data

    def sair(self):
        self.persistencia.sair(self.dict)

    def adicionar_contato(self, nome: str, telefone: str) -> None:
        self.dict[nome] = telefone

    def remover_contato(self, nome: str) -> None:
        try:
            del self.dict[nome]
        except KeyError:
            raise ValueError('Contato não encontrado.')

    def buscar_contato(self, nome: str) -> dict:

        if nome in self.dict:
            return nome, self.dict[nome]
        else:
            raise ValueError('Contato não encontrado.')
