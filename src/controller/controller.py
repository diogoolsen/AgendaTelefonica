
from ..model import Agenda


class Controller():
    def __init__(self):
        self.agenda = Agenda()

    def sair(self):
        self.agenda.sair()

    def search_contact(self, name):
        try:
            nome, telefone = self.agenda.buscar_contato(name)
        except ValueError as err:
            return ('ALERT', str(err))
        else:
            return ('CONTACT', (nome, telefone))

    def add_contact(self,
                    name: str,
                    telefone: str) -> None:
        try:
            self.agenda.adicionar_contato(name, telefone)
        except ValueError as err:
            return ('ALERT', str(err))
        else:
            return ('MSG', 'Contato inserido.')

    def remove_contact(self, name) -> None:
        try:
            self.agenda.remover_contato(name)
        except ValueError as err:
            return ('ALERT', str(err))
        else:
            return ('MSG', 'Contato removido.')
