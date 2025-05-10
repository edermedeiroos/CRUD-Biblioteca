import json
# TODO - Transfer .txt data to .json

# Verify if archive exist
def arquivoexiste(nome):
    try:
        with open(nome, 'r+', encoding='utf-8') as arquivo:
            if bool(arquivo.read()) == False: # Checks if .json is empty
                json.dump(obj = [], fp=arquivo, ensure_ascii=False, indent=2)

    except (FileNotFoundError):
        return False

    else:
        return True

# Create archive.
def criararquivo(nome):
    try:
        with open(nome, 'w', encoding='utf-8') as arquivo:
            json.dump(obj = [], fp=arquivo, ensure_ascii=False, indent=2) # dump json with a list.

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

    # Verify if book has already been added
    with open(arquivo, 'r+', encoding='utf-8') as arquivo_json:
        loaded = json.load(arquivo_json)
        for dicionario in loaded: 
            if str(livro).upper().replace(' ', '') == str(dicionario).upper().replace(' ', ''):
                verificacao_livro = True 

    if verificacao_livro:
        return "*Livro já adicionado*"

    else:

        # Dump list loaded with old .json, updated with new book
        lista_livros.append(livro.copy())
        with open(arquivo, 'w+', encoding='utf-8') as arquivo_json:
            json.dump(lista_livros, fp=arquivo_json, ensure_ascii=False, indent=2)
            return "Livro adicionado."

# def function visualize book.
def visualizar(data, start=0):
    indice = 1

    # Show archieve formated
    for dicionario in data[start:]:
        print(f'{indice}. {dicionario}'
                .replace('{', '').replace('}', '')
                .replace("'", '').replace(', ', ' | '))
        indice += 1

# def function update book.
def atualizar(indice_livro, atributo, novo_atributo):
    lista_livros[indice_livro - 1][atributo] = novo_atributo # Update book list with parameters

    # Dump json with new book list
    with open(arquivo, 'w+', encoding='utf-8') as arquivo_json:
        json.dump(lista_livros, fp=arquivo_json, ensure_ascii=False, indent=2)
        return "Livro atualizado."

# def function search book.
def buscar(atributo, procurado):
    achados = []

    with open(arquivo, 'r', encoding='utf-8') as arquivo_json:
        loaded = json.load(arquivo_json)

        if atributo not in livro.keys(): # Checks if atribute exists
            return False
        
        for dicionario in loaded: # Search in dictionarys for the atribute
            if dicionario[atributo].upper() == procurado.upper():
                achados.append(dicionario) # If founded, append the dict to found list.
        
    return achados
                

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
    'NUMERO DE PAGINAS': '',
    'EDITORA': '',
    'ISBN': ''
}

# Loads .json to list
with open(arquivo, 'r+', encoding='utf-8') as arquivo_json:
    lista_livros = json.load(arquivo_json)

# Interation menu.
while True:
    print(f'\n{"BIBLIOTECA":^150}\n{"-"*150}')
    menu(opcoes)
    print()

    # Verify choice type raising error in except ValueError/TypeError
    try:
        opcao = int(input(" - Opção desejada [-1 p/ sair]: "))
        print()

    except (ValueError, TypeError):
        print(f'{"<DIGITE APENAS NÚMEROS>":^150}\n')
        continue

    else:

        # Execute add book function
        if opcao == 1:
            print(f'{"<Adicionar Livro>":^150}\n')

            for atributo in livro.keys():
                livro[atributo] = input(f" - {atributo}: ").strip() # Add each atribute to the dictionary

            print()
            print(adicionar(livro))

        # Execute visualize books function
        elif opcao == 2:
            print(f'{"<Livros>":^150}\n')
            with open(arquivo, 'r', encoding='utf-8') as arquivo_json:
                loaded = json.load(arquivo_json)
                visualizar(loaded)

        # Execute update book function
        elif opcao == 3:
            print(f'{"<Atualizar Livro>":^150}\n')
            with open(arquivo, 'r', encoding='utf-8') as arquivo_json:
                loaded = json.load(arquivo_json)
                visualizar(loaded) # Visualize books function
            print()

            # Verify index choice type raising error in except ValueError/TypeError
            try:
                item = int(input('- Livro para atualização [índice]: '))
                with open(arquivo, 'r', encoding='utf-8') as arquivo_json:
                    loaded = json.load(arquivo_json)

                if item not in range(1, len(loaded) + 1): # Verify if index is in the json range.
                    raise IndexError

            except (ValueError, TypeError):
                print("\n*Digite apenas números*\n")

            except(IndexError):
                print("\n*Índice do livro desconhecido*\n")
            
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
            print(f"ATRIBUTOS: {list(livro.keys())}\n".replace("'", ""))

            nome_atributo = input('- Atributo para busca: ').strip().upper()
            atributo_procurado = input(f'- Pesquisa ({nome_atributo}): ').strip()

            resultado = buscar(nome_atributo, atributo_procurado)

            if bool(resultado) == False:
                print("*Não foram achados resultados para pesquisa*")
            
            else:
                print(f"\nForam achados {len(resultado)} resultados para sua pesquisa: \n")
                visualizar(resultado)


        # Execute delete book function
        elif opcao == 5:
            print(f'{"<Deletar Livro>":^150}\n')
            deletar()

        # End program option
        elif opcao == -1:
            print(f'{"<ENCERRANDO SISTEMA>":^150}\n')
            break

        # User's choice out of the choice's range.
        else:
            print(f'{"<OPÇÃO INEXISTENTE>":^150}\n')