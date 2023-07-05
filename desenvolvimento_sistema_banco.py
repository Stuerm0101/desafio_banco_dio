menu="""
----------------------------------------
==================MENU==================
[s] para realizar o saque
[d] para realizar um depósito
[e] para tirar o extrato
[q] para sair
----------------------------------------
"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE=3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("A opração falhou! O valor informado é inválido")    
    
    elif opcao == "s":
        valor=float(input("Informe o valor a ser sacado"))
        

    elif opcao == "e":
        print("\n***************** EXTRATO *****************")
        print("Nao foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
    
    elif opcao == "q":
        break        
    else:
        print("Digite um valor válido para que possamos prosseguir")
        continue