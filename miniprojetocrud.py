# -*- coding: utf-8 -*-
"""miniprojetocrud.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TLySRNXiI5qRlI9lrrP43VgAZef65XMT

# CREATE
"""

# Dicionário para armazenar os livros
livros = dict()

# Função para adicionar um novo livro ao acervo
def criar_novo_produto():
  nome = input("Qual o nome do livro? ")
  nome = nome.upper()
  genero = input("Qual o genero do livro? ")
  genero = genero.upper()
  autor = input("Qual o autor do livro? ")
  autor = autor.upper()
  ano = int(input("Qual o ano do livro? "))
  quantidade = int(input("Qual a quantidade disponivel do livro? "))

# Adiciona os detalhes do livro ao dicionário
  livros[nome] = { "nome": nome , "autor" : autor, "genero" : genero, "ano" : ano, "quantidade" : quantidade }
  print("livro cadastrado com sucesso!")

criar_novo_produto()

"""# READ

"""

# Função para listar todos os livros cadastrados
def listar_livros():
  if not livros:
    print("Não há livros cadastrados")
  else:
    print("produtos cadastrados")
    for chave, valor in livros.items():
      print(f"produto: {chave}, genero: {valor['genero']}, autor: {valor['autor']}, ano:{valor['ano']}, quantidade: {valor['quantidade']} ")

listar_livros()

"""# READ livro especifico


"""

# Função para listar um livro específico
def listar_livros_especifico():
  livro_especifico = input("Qual livro deseja listar? ")
  livro_especifico = livro_especifico.upper()

  if livro_especifico in livros:
    detalhes = livros[livro_especifico]
    print(f"produto: {detalhes['nome']}, genero: {detalhes['genero']}, autor: {detalhes['autor']}, ano:{detalhes['ano']}, quantidade: {detalhes['quantidade']} ")
  else:
    print("livro não encontrado")

listar_livros_especifico()

"""# UPDATE

"""

# Função para atualizar os dados de um livro
def atualizar_livro():
  livro_atualizar = input("Qual livro deseja atualizar? ")
  livro_atualizar = livro_atualizar.upper()

# Atualiza o campo selecionado

  if livro_atualizar in livros:
    detalhes = livros[livro_atualizar]
    dados_edit = input("Qual dado deseja atualizar?\n1. Nome:\n2. Genero:\n3 Autor:\n3 Ano:\n4 Quantidade:\n ")
    if dados_edit == "1":
        detalhes["nome"] = input("Digite o novo nome: ")
    elif dados_edit == "2":
        detalhes["genero"] = input("Digite o novo genero: ")
    elif dados_edit == "3":
        detalhes["autot"] = input("Digite o novo autor: ")
    elif dados_edit == "4":
        detalhes["quantidade"] = input("Digite a nova quantidade: ")
    else:
        print("Opção invalida")
  else:
    print("Livro nao encontado")

atualizar_livro()

"""# DELETE"""

# Função para deletar um livro do acervo
def deletar_livro():
  livro_deletar = input("Qual livro deseja deletar? ")
  livro_deletar = livro_deletar.upper()
  if livro_deletar in livros:
    del livros[livro_deletar]
    print("livro deletado com sucesso")
  else:
    print("livro não encontrado")

deletar_livro()

"""# Interface"""

def interface():
  while True:
    print("\n1 Adicionar livro:\n2 Listar livros:\n3 Listar livro especifico:\n4 Atualizar livro:\n5 Deletar livro:\n6 Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
      criar_novo_produto()
    elif opcao == "2":
      listar_livros()
    elif opcao == "3":
      listar_livros_especifico
    elif opcao == "4":
      atualizar_livro()
    elif opcao == "5":
      deletar_livro()
    elif opcao == "6":
      print("saindo do programa...")
      break
    else:
        print("Opção invalida")

interface()
