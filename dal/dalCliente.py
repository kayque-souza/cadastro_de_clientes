from model.modelCliente import Cliente

class ClienteDal:
    @classmethod
    def salvarCliente(cls, cliente: Cliente):
        with open('clientes.txt', 'w') as arq:
            arq.write("nome = " + cliente.nome + " | sobrenome = " + cliente.sobrenome + " | idade = " + str(cliente.idade) + " | CPF = " + cliente.cpf + "\n")
            arq.write("username = " + cliente.username + " | password = " + cliente.password + "\n")
    
    @classmethod
    def buscarCliente(cls):
        with open('clientes.txt', 'r') as arq:
            pessoa = arq.read().strip().split(" ")

        return Cliente(pessoa[0], pessoa[1], pessoa[2], pessoa[3], pessoa[4], pessoa[5])