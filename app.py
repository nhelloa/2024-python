clientes = []

def cadastro_clientes():
    print('Cadastrar Clientes')
    nome = input('Nome do Cliente: ')
    email = input('Email do Cliente: ')
    telefone = input('Telefone do Cliente: ')
    endereço = input('Endereço do cliente: ')
    # Adicionar o código para cadastro de clientes
    cliente = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'endereço': endereço,
        'ativo': True
    }

    clientes.append(cliente)
    print('Cliente cadastrado com sucesso!')

def listar_clientes():
# Aqui você pode adicionar o código para listar clientes
    print('Listar Clientes')
    if clientes:
        for idx, cliente in enumerate(clientes):
            status = 'Ativo' if cliente['ativo'] else 'Inativo'
            print(f' {idx + 1}. Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone : {cliente['telefone']}, Status: {status}')
    else:
        print('Nenhum cliente cadastrado.\n')

def ativar_cliente():
# Adicionar o código para ativar ou desativar clientes
    print('Ativar/Desativar Cliente')
    listar_clientes()
    if clientes:
        try:
            cliente_id = int(input('Escolha o número do cliente para ativar/desativar: '))
            if 1 <= cliente_id <= len(clientes):
                cliente = clientes[cliente_id - 1]
                cliente['ativo'] = not cliente['ativo']
                print(f"Cliente {cliente['nome']} agora está {'Ativo' if cliente['ativo'] else 'Inativo'}.\n")
            else:
                print('Cliente não encontrado!\n')
        except ValueError:
            print('Entrada inválida! Por favor, inserir número válido.\n')

def sair_aplicacao():
     # Adicionar o código para encerrar a aplicação
    print('Saindo da Aplicação')
    exit()

def exibir_menu():
    print('''
      
          X-SPORT
          
          1. Cadastro de Clientes
          2. Listar Clientes
          3. Ativar Cliente
          4. Sair da aplicação
          
      ''')

while True:
    exibir_menu()
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastro_clientes()
        elif opcao_escolhida == 2:
            listar_clientes()
        elif opcao_escolhida == 3:
            ativar_cliente()
        elif opcao_escolhida == 4:
            sair_aplicacao()
            break  # Sair do loop para encerrar o programa
        else:
            print('Opção inválida! Por favor, escolha uma opção entre 1 e 4.')
    except ValueError:
        print('Entrada inválida! Por favor, inserir número válido.')
