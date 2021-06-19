from .controller import Controller
# from .model import Agenda
# from .model import Persistencia
from .view import GUI
from .view import Menu


class Main():
    def __init__(self, ui='GUI') -> None:
        self.controller = Controller()

        if ui == 'GUI':
            self.ui = GUI(self.controller)
        elif ui == 'TUI':
            self.ui = Menu(self.controller)
        else:
            raise RuntimeError('Interface com usuário inválida')

        self.ui.run()
