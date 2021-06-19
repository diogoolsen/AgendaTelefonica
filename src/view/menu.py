

class Menu():

    def __init__(self, controller) -> None:
        self.controller = controller

    def print_header(self) -> None:

        print('\n'*15)
        self.print_line()
        print('|{:^48s}|'.format('AGENDA'))
        self.print_line()

    def print_sub_header(self, text: str) -> None:

        print('|{:^48s}|'.format(text))
        self.print_line()

    def print_line(self) -> None:

        line = '+' + '-'*48 + '+'
        print(line)

    def print_item(self, text: str) -> None:

        print('| {:<47s}|'.format(text))

    def print_alert(self, text: str) -> None:

        self.print_line()
        self.print_sub_header('ALERTA')
        self.print_sub_header(text)

    def print_message(self, text: str) -> None:

        self.print_line()
        self.print_sub_header('Mensagem')
        self.print_sub_header(text)

    def _continue(self) -> None:

        input('Digite uma tecla para continuar')
        self.show_main_menu()

    def show_main_menu(self) -> None:

        self.print_header()
        self.print_item('1 - Pesquisar')
        self.print_item('2 - Adicionar')
        self.print_item('3 - Remover')
        self.print_item('4 - Sair')
        self.print_line()
        self.get_main_opc()

    def get_main_opc(self) -> None:

        opc = input('Digite sua opção: ')

        if opc == '1':
            self.show_search_menu()
        elif opc == '2':
            self.show_add_menu()
        elif opc == '3':
            self.show_remove_menu()
        elif opc == '4':
            self.exit()
        else:
            self.show_main_menu()

    def show_search_menu(self) -> None:

        self.print_header()
        self.print_sub_header('Buscando contato')
        name = input('Nome: ')

        returned = self.controller.search_contact(name)
        self.eval(returned)

        self._continue()

    def show_add_menu(self):

        self.print_header()
        self.print_sub_header('Adicionando contato')

        name = input('Nome: ')
        telefone = input('Telefone: ')

        returned = self.controller.add_contact(name, telefone)
        self.eval(returned)

        self._continue()

    def show_remove_menu(self):

        self.print_header()
        self.print_sub_header('Removendo contato')
        name = input('Nome: ')

        returned = self.controller.remove_contact(name)
        self.eval(returned)

        self._continue()

    def print_contact(self, nome, telefone) -> None:

        print('\tNome: ', nome)
        print('\tTelefone: ', telefone)
        print('')

    def eval(self, returned) -> None:

        if returned[0] == 'ALERT':
            self.print_alert(returned[1])
        elif returned[0] == 'MSG':
            self.print_message(returned[1])
        elif returned[0] == 'CONTACT':
            self.print_contact(returned[1][0], returned[1][1])

    def run(self) -> None:
        self.show_main_menu()

    def exit(self) -> None:

        self.print_message('Saindo')
        self.controller.sair()
