
import sys
import tkinter as tk
from tkinter import messagebox


class GUI():
    def __init__(self, controller):
        self.root = tk.Tk()
        self.root.geometry('600x400')

        self.controller = controller

        self.createFrameAdd()
        self.createFrameDel()
        self.createFrameSearch()

        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.bind('<Escape>', self.exit)

    def show_add(self):
        self.frame_add.tkraise()

    def show_del(self):
        self.frame_del.tkraise()

    def show_srch(self):
        self.frame_srch.tkraise()

    def createFrameAdd(self):
        self.frame_add = tk.Frame(self.root)
        self.frame_add.grid(row=0, column=0)

        label_name = tk.Label(self.frame_add, width=20, text='Nome:')
        label_name.grid(row=0, column=0)

        self.add_nome = tk.Entry(self.frame_add, width=20)
        self.add_nome.grid(row=0, column=1)

        label_tel = tk.Label(self.frame_add, width=20, text='Telefone:')
        label_tel.grid(row=1, column=0)

        self.add_telefone = tk.Entry(self.frame_add, width=20)
        self.add_telefone.grid(row=1, column=1)

        button = tk.Button(self.frame_add,
                           text='Adicionar',
                           width=20,
                           command=self.add_contact)
        button.grid(row=2, column=1)

        button_del = tk.Button(self.frame_add,
                               text='Tela Remover',
                               width=20,
                               command=self.show_del)
        button_del.grid(row=3, column=0)

        button_srch = tk.Button(self.frame_add,
                                text='Tela Buscar',
                                width=20,
                                command=self.show_srch)
        button_srch.grid(row=3, column=1)

    def add_contact(self):
        returned = self.controller.add_contact(self.add_nome.get(),
                                               self.add_telefone.get())
        self.eval(returned)

    def createFrameDel(self):
        self.frame_del = tk.Frame(self.root)
        self.frame_del.grid(row=0, column=0)

        label = tk.Label(self.frame_del, width=20, text='Nome:')
        label.grid(row=0, column=0)

        self.del_nome = tk.Entry(self.frame_del, width=20)
        self.del_nome.grid(row=0, column=1)

        label_tel = tk.Label(self.frame_del, width=20, text='')
        label_tel.grid(row=1, column=0)

        button = tk.Button(self.frame_del,
                           text='Remover',
                           width=20,
                           command=self.del_contact)
        button.grid(row=2, column=1)

        button_add = tk.Button(self.frame_del,
                               text='Tela Adicionar',
                               width=20,
                               command=self.show_add)
        button_add.grid(row=3, column=0)

        button_srch = tk.Button(self.frame_del,
                                text='Tela Buscar',
                                width=20,
                                command=self.show_srch)
        button_srch.grid(row=3, column=1)

    def del_contact(self):
        returned = self.controller.remove_contact(self.del_nome.get())
        self.eval(returned)

    def createFrameSearch(self):
        self.frame_srch = tk.Frame(self.root)
        self.frame_srch.grid(row=0, column=0)

        label = tk.Label(self.frame_srch, width=20, text='Nome:')
        label.grid(row=0, column=0)

        self.srch_nome = tk.Entry(self.frame_srch, width=20)
        self.srch_nome.grid(row=0, column=1)

        label_tel = tk.Label(self.frame_srch, width=20, text='')
        label_tel.grid(row=1, column=0)

        button = tk.Button(self.frame_srch,
                           text='Buscar',
                           width=20,
                           command=self.srch_contact)
        button.grid(row=2, column=1)

        button_add = tk.Button(self.frame_srch,
                               text='Tela Adicionar',
                               width=20,
                               command=self.show_add)
        button_add.grid(row=3, column=0)

        button_del = tk.Button(self.frame_srch,
                               text='Tela Remover',
                               width=20,
                               command=self.show_del)
        button_del.grid(row=3, column=1)

    def srch_contact(self):
        returned = self.controller.search_contact(self.srch_nome.get())
        self.eval(returned)

    def showInfo(self, msg):
        messagebox.showinfo('Informação', msg)

    def showWarning(self, msg):
        messagebox.showwarning('Warning', msg)

    def eval(self, returned) -> None:

        if returned[0] == 'ALERT':
            self.showWarning(returned[1])
        elif returned[0] == 'MSG':
            self.showInfo(returned[1])
        elif returned[0] == 'CONTACT':
            self.showInfo('Nome: ' + str(returned[1][0]) + '\n' +
                          'Telefone:' + str(returned[1][1]))

    def run(self) -> None:
        self.root.mainloop()

    def exit(self, evento=None):
        self.controller.sair()
        sys.exit()
