import os

def cadastro_de_clientes():
    print('\nVocê está no cadastro de clientes')
    
    nome = input('Digite o nome do cliente: ')
    idade = input('Digite a idade do cliente: ')
    email = input('Digite o email do cliente: ')
    print(f'Dados do cliente cadastrados: Nome: {nome}, Idade: {idade}, Email: {email}\n')

    
    modo_variavel = 'a' if os.path.exists('clientes.txt') else 'w'
    abrir_arquivo = open('clientes.txt', modo_variavel)
    abrir_arquivo.write(f'Nome: {nome}, Idade: {idade}, Email: {email}\n')
    abrir_arquivo.close()