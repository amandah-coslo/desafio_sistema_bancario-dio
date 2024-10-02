
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 1:
        print("Depósito")
        # DEPOSITO = inteiro e valores positivos, todos os depósitos devem 
        # ser armazenados em uma variável e exibidos na operação de extrato

        valor = float(input("Informe o valor do depósito: ")) 

        if valor > 0: # Somente valores positivos
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação inválida! O valor informado não corresponde.")

    elif opcao == 2:
        print("Saque")
        # SAQUE = 3 saques diários com limite máximo de R$ 500,00 por saque. 
        # Caso o usuário não tenha saldo em conta, o sistema deve exibir uma 
        # mensagem informando que não será possível sacar por falta de saldo. 
        # Todos os saques devem ser armazenados em uma variável e exibidos na 
        # operação de extrato.

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo # Não tem saldo suficiente

        excedeu_limite = valor > limite # Valor do saque excede o limite máximo de R$ 500,00 por saque

        excedeu_saques = numero_saques >= LIMITE_SAQUES # Número máximo de saques excedido

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite máximo de R$ 500,00 por saque.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação inválida! O valor informado não corresponde.")

    elif opcao == 3:
        print("Extrato")
        # EXTRATO = devem listar todos os depósitos e saques realizados na conta. 
        # No fim da listagem deve ser exibido o saldo atual da conta. Os valores 
        # devem ser exibidos utilizando o formato R$ XXX.XX 
        # (ex: 1500.45 = R$ 1500.45)

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 0:
        break 
    
    else:
        print("Operação inválida! Por favor, selecione novamente a opeção desejada.")