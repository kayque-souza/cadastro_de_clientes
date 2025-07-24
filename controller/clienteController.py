from dal.dalCliente import ClienteDal
from model.modelCliente import Cliente

class ClienteController:
    
    @classmethod
    def cadastrarCliente(cls):
        print('')
        nome = input('Digite o seu nome: ')
        sobrenome = input('Digite o seu sobrenome: ')
        idade = int(input('Digite sua idade: '))
        cpf = input('Digite o seu cpf: ')
        username = input('Digite um nome de usuário: ')
        password = input('Digite sua senha: ')

        return nome, sobrenome, idade, cpf, username, password

    @classmethod
    def verificarCadastro(cls, nome, sobrenome, idade, cpf, username, password):
        if len(nome) > 3 and (idade > 0 and idade < 200) and len(cpf) == 11:
            try:
                ClienteDal.salvarCliente(Cliente(nome, sobrenome, idade, cpf, username, password))
                return True
            except:  # noqa: E722
                return False