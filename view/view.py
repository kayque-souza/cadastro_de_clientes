from controller.clienteController import ClienteController

def main():
    while True:
        print('=========== Menu ===========')
        print('1. Clientes')
        print('2. Produtos')
        print('3. Sair')
        print('=============================')

        opcao = input('Escolha uma opção: ')
            
        if opcao == '1':
            while True:
                print('\nVocê escolheu a opção de clientes.')
                print('1. Cadastrar Cliente')
                print('2. Voltar ao Menu Principal')
                
                sub_opcao = input('Escolha uma opção: ')
                
                if sub_opcao == '1':
                    cadastro = ClienteController.cadastrarCliente()
                    
                    ClienteController.verificarCadastro(cadastro[0], cadastro[1], cadastro[2], cadastro[3], cadastro[4], cadastro[5])
                elif sub_opcao == '2':
                    print('Voltando ao menu principal...\n')
                    break
                else:
                    print('Opção inválida, tente novamente.')

        elif opcao == '2':
            print('Você escolheu a opção de produtos. (Funcionalidade ainda não implementada)\n')

        elif opcao == '3':
            print('Saindo...')
            break
        else:
            print('Opção inválida, tente novamente.')