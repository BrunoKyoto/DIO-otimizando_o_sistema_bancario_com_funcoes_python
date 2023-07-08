# Menu referente ao segundo laço de repetição: simulando a entrada do cliente na conta após confirmar seus dados.
def menu():
    menu = """\n
    ----------- MENU -----------
    ------ CONTA CORRENTE ------
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    => """
    return input(menu)

# Menu referente ao primeiro laço de repetição
def menu_cadastro():
    menu = """\n
    ----------- MENU -----------
    ---------- ACESSO ----------
    [1] Cadastrar usuário
    [2] Cadastrar conta
    [3] Acessar conta
    [4] Sair    
    => """
    return input(menu)

# Função responsável por executar o saque diretamente do saldo da conta e fazer validações gerais, conforme regras:
# limite de 3 saques diários; limite máximo para saque unitário: R$500,00 e limite de saldo da conta.
def sacar(*, valor, saldo, limite_por_saque, LIMITE_SAQUES, numero_saques, extrato):
    excedeu_limite_saques = numero_saques >= LIMITE_SAQUES
    excedeu_valor_maximo_por_saque = valor > limite_por_saque
    excedeu_saldo = valor > saldo

    if excedeu_limite_saques:
                    print("Operação negada. Você excedeu a quantidade permitida de saques diários.")
    
    elif excedeu_valor_maximo_por_saque:
                    print("Operação negada. O valor excedeu a quantia máxima permitida por saque.")

    elif excedeu_saldo:
                    print("Operação negada. O valor excedeu o saldo disponível.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
        print("\n### Saque realizado com sucesso! ###")
    else:
        print("Operação negada. O valor informado é inválido.")

    return saldo, extrato, numero_saques

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print(f"\n### Depósito realizado com sucesso! ###")
    else:
        print("Operação não permitida! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n################ EXTRATO ################")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("#########################################")

# Função de cadastro de usuário com base em número de CPF - apenas CPFs únicos podem ser cadastrados.
def criar_usuario(usuarios):
    cpf = input("\nInforme seu número de CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário cadastrado com esse CPF.")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n### Usuário criado com sucesso! Siga para a criação de conta ###")

# Função auxiliar que verifica a existência de um determinado CPF na lista "usuarios".
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n### Conta criada com sucesso! ###")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado! Processo de criação de conta encerrado.")

def acessar_conta(contas, usuarios, prosseguir):
    cpf = input("\nInforme o cpf do titular (somente números): ")
    filtrando_usuario = filtrar_usuario(cpf, usuarios)
    for conta in contas:
        if conta['usuario'] == filtrando_usuario:
            linha = f"""
                ###################################
                CONTA LOCALIZADA! ACESSO PERMITIDO!
                ###################################
                Agência: {conta['agencia']}
                C/C: {conta['numero_conta']}
                Titular: {conta['usuario']['nome']}
                ###################################
            """
            print(linha)
            prosseguir = True
            return prosseguir
    else:
        print("\nUsuário não encontrado.")

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite_por_saque = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    prosseguir = False

    # Primeiro loop: criação de usuário e conta
    while True:

        opcao = menu_cadastro()

        if opcao == "1":
            criar_usuario(usuarios)
        
        elif opcao == "2":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "3":
            prosseguir = acessar_conta(contas, usuarios, prosseguir)
            if prosseguir:
                 break

        elif opcao == "4":
            break

        else:
            print("Operação inválida! Por favor, selecione novamente a operação desejada.")

    # A variável "prosseguir" serve para validar se a conta foi localizada. Após a localização da mesma, "prosseguir" é modificada para "True".
    # Nesse ponto, "prosseguir" é validada e se "True", inicia-se o segundo loop, onde ocorre a movimentação de conta.
    if prosseguir:

        while True:

            opcao = menu()

            if opcao == "1":
                valor = float(input("Informe o valor do depósito: "))

                saldo, extrato = depositar(valor, saldo, extrato)

            elif opcao == "2":
                valor = float(input("Informe o valor do saque: "))

                saldo, extrato, numero_saques = sacar(
                    valor = valor,
                    saldo = saldo,
                    limite_por_saque = limite_por_saque,
                    LIMITE_SAQUES = LIMITE_SAQUES,
                    numero_saques = numero_saques,
                    extrato = extrato)
            
            elif opcao == "3":
                exibir_extrato(saldo, extrato = extrato)

            elif opcao == "4":
                print("\nObrigado por utilizar nossos serviços!\n")
                break

            else:
                print("Operação inválida! Por favor, selecione novamente a operação desejada.")

# Inicia a execução do script
main()