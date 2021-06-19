
from os.path import exists, getsize

import pickle


class Persistencia:

    def __init__(self) -> None:

        self.file_name = 'contatos.pkl'
        self.contact_data = {}

        self.carregar_agenda()

    def sair(self, dict) -> None:
        self.contact_data = dict

        self.gravar_agenda()

    def carregar_agenda(self) -> None:

        if exists(self.file_name) and getsize(self.file_name) > 0:
            with open(self.file_name, 'rb') as file:
                self.contact_data = pickle.load(file)

    def gravar_agenda(self) -> None:

        with open(self.file_name, 'wb') as file:
            pickle.dump(self.contact_data, file)
