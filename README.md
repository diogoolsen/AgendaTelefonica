# Agenda Telefónica

O programa usa dicionários para armazenar os pares Nome (chave) e Telefone (valor), viabilizando as operações de inserir contato, buscar contato e remover contato. O sistema apresenta duas opções de interface com o usuário, uma de texto e outra gráfica, implementada com o Tkinter - https://docs.python.org/3/library/tkinter.html. A persistência da agenda é viabilizada através da biblioteca Pickle - https://docs.python.org/3/library/pickle.html - a qual salva/carrega o dicionário (que armazena os pares Nome: Telefone) em disco. O Código foi desenvolvido de acordo com o guia de estilo de codificação PEP-8 - https://www.python.org/dev/peps/pep-0008/.



### MVC

A agenda foi implementada no padrão MVC que implementa os pacotes:

- **Model**: Model do padrão MVC - implementa as regras de negócio.
  - Classe **Agenda**: Implementa o processamento da agenda - inserir, buscar e remover;
  - Classe **Persistência**: Implementa a persistência da agenda com a bilioteca Pickle;
- **Controller**: Controller do padrão MVC - faz a intermediação entre as regras de negócio e as interfaces implementadas.
- **View**: Implementa as interfaces:
  - Classe **GUI**: (*Graphical User Interface* - Interface Gráfica do Usuário) implementada com a biblioteca Tkinter.
  - Classe **Menu**: Implementa uma interface Texto para a mesma agenda, mostrando a possibilidade de trocas de interface que o MVC oferta ao desacoplar as regras de negócio da interface.