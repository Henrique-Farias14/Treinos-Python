import time
opcao = 0
saldo = 100

while opcao != 4:
    print("=== Caixa Eletrônico ===")
    print("1 - Consultar Saldo")
    print("2 - Depositar Dinheiro")
    print("3 - Sacar Dinheiro")
    print("4 - sair")
    try:
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                print("Saldo: R$", round(saldo, 2))
            case 2:
                print("Saldo atual: R$", round(saldo, 2))
                print("Quanto deseja depositar?")
                try:
                    deposito = float(input("Deposito: R$"))
                    if deposito > 0:
                        print("Depositando...")
                        time.sleep(1)
                        saldo += deposito
                        print("Novo saldo: R$", round(saldo, 2))
                    else:
                        print("Registrando...")
                        time.sleep(1)
                        print("Valor invalido!")
                        print("Tente novamente!")
                except ValueError:
                    print("Essa não é uma opção!")
                    print("Tente novamente!")
            case 3:
                print("Saldo atual: R$", round(saldo, 2))
                print("Quanto deseja sacar?")
                try:
                    saque = float(input("Sacar: R$"))
                    if saque > saldo or saque <= 0:
                        print("Registrando...")
                        time.sleep(1)
                        print("Valor invalido!")
                        print("Tente novamente!")
                    else:
                        print("Registrando...")
                        time.sleep(1)
                        saldo -= saque
                        print("Novo saldo: R$", round(saldo, 2))
                except ValueError:
                    print("Essa não é uma opção!")
                    print("Tente novamente!")
            case 4:
                print("Encerrando o programa...")
            case _:
                print("Opção invalida!")
                print("Tente novamente!")
    except ValueError:
        print("Essa não é uma opção!")
        print("Tente novamente!")