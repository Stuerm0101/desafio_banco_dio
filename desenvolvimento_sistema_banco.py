menu="""
----------------------------------------
==================MENU==================
[s] para realizar o saque
[d] para realizar um depósito
[e] para tirar o extrato
[q] para sair
----------------------------------------
"""
regras_de_uso = """
Regras do banco:
--------------------------------------------------------------------------
O valor máximo de saque é de R$500
Só podem ser realizados um máximo de 3 saques por dia 
Caso não haja saldo em sua conta a operação de saque ficará indisponível
--------------------------------------------------------------------------
Agradecemos a compreensão
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    print(regras_de_uso)
    
    opcao = input(menu)

    
    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("A opração falhou! O valor informado é inválido")    
    
    elif opcao == "s":
        valor=float(input("Informe o valor a ser sacado: "))
        
        if valor > limite:
            print("O valor de saque não pode exceder o limite de R$500\n")
            situacao_aprovado = False

        elif valor > saldo:
            print("Você não tem saldo disponível em sua conta\n")
            situacao_aprovado = False

        elif numero_saques == LIMITE_SAQUE:
            print("Você ja antingiu o limite de saques em um dia\n")
            situacao_aprovado = False

        else:
            situacao_aprovado = True

        if situacao_aprovado and valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou verifique os dados informados e tente novamente")    

    elif opcao == "e":
        print("\n***************** EXTRATO *****************")
        print("Nao foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
    
    elif opcao == "q":
        break        
    else:
        print("Digite um valor válido para que possamos prosseguir")
        continue