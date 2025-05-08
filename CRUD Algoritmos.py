import json
# TODO - Transfer .txt data to .json

# Verify if archive exist
def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()

    except FileNotFoundError:
        return False

    else:
        return True

# Create archive.
def criararquivo(nome):
    try:
        a = open(nome, 'wt+').write(' - Livros: \n')
        a.close()

    except:
        print('Falha na criação do arquivo')

# Default menu print.
def menu(opcoes):
    indice = 1

    for opcao in opcoes:
        print(f"[{indice}] {opcao}")
        indice += 1

# def function add book.
def adicionar(livro):
    verificacao_livro = False

    with open(arquivo, 'r+', encoding='utf-8') as txt:
        for linha in txt.readlines(): 
            if (f'{livro}\n').upper().replace(' ', '') == linha.upper().replace(' ', ''):
                verificacao_livro = True

    if verificacao_livro:
        return "*Livro já adicionado*"

    else:
        with open(arquivo, 'a+', encoding='utf-8') as txt:
            txt.write(f'{livro}\n')
            return f"Livro adicionado."

# def function visualize book.
def visualizar():
    indice = 1

    with open(arquivo, 'r', encoding='utf-8') as txt:
        for linha in txt.readlines():
            print(f'{indice}. {linha}')
            indice += 1

# def function update book.
def atualizar(indice_livro, atributo, novo_atributo):
    with open(arquivo, 'r+', encoding='utf-8') as txt:
        foi_atualizado = False
        indice = 1

        for linha in txt.readlines(): # rewrites txt

            if indice_livro == indice: # Checks if line corresponds to book index
                print(linha)
                print(atributo)
                print(novo_atributo)
                txt.seek(0, 0)
                txt.write(linha.replace(atributo, novo_atributo))

                foi_atualizado = True

            else:
                txt.seek(0, 0)
                txt.write(linha)
                print(linha)
            
            indice += 1

        if foi_atualizado:
            return "Livro atualizado."
        return "*Livro para atualização não encontrado*"


# def function search book.
def buscar():
    ''

# def function delete book.
def deletar():
    ''

# archive verification/creation
arquivo = "biblioteca.json"
if not arquivoexiste(arquivo):
    criararquivo(arquivo)
    print(f'Arquivo "{arquivo}" criado.')

# variables declaration
opcoes = ["Adicionar Livro", "Visualizar Livros", "Atualizar Livro", "Buscar Livro", "Deletar Livro"]
livro = {
    'NOME': '',
    'AUTOR': '',
    'ASSUNTO': '',
    'NÚMERO DE PÁGINAS': '',
    'EDITORA': '',
    'ISBN': ''
}

# Interation menu.
while True:
    print(f'{"BIBLIOTECA":^150}\n{"-"*150}')
    menu(opcoes)
    print()

    # Verify choice type raising error in except ValueError/TypeError
    try:
        opcao = int(input(" - Opção desejada: "))
        print()

    except (ValueError, TypeError):
        print(f'{"<DIGITE APENAS NÚMEROS>":^150}\n')
        continue

    else:

        # Execute add book function
        if opcao == 1:
            print(f'{"<Adicionar Livro>":^150}\n')

            for atributo in livro.keys():
                livro[atributo] = input(f" - {atributo}: ") # Add each atribute to the dictionary

            print()
            print(adicionar(livro))

        # Execute visualize books function
        elif opcao == 2:
            print(f'{"<Livros>":^150}\n')
            visualizar() 

        # Execute update book function
        elif opcao == 3:
            print(f'{"<Atualizar Livro>":^150}\n')
            visualizar()

            # Verify index choice type raising error in except ValueError/TypeError
            try:
                item = int(input('- Livro para atualização [índice]: '))

            except (ValueError, TypeError):
                print("\n*Digite apenas números*\n")
            
            else:
                atributo = input('- Atributo para atualização: ').upper().strip() # Choose attribute to update

                if atributo not in livro.keys(): # Check if attribute exists
                    print("\n*Atributo Desconhecido*\n")
                
                else:
                    novo_atributo = input(f'- Novo {atributo}: ') # Get new attribute
                    print(atualizar(item, atributo, novo_atributo))

        # Execute search book function
        elif opcao == 4:
            print(f'{"<Buscar Livro>":^150}\n')
            buscar()

        # Execute delete book function
        elif opcao == 5:
            print(f'{"<Deletar Livro>":^150}\n')
            deletar()

        # User's choice out of the choice's range.
        else:
            print(f'{"<OPÇÃO INEXISTENTE>":^150}\n')