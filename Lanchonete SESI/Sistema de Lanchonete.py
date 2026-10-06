import time

continuar = "1"
itens = 0
valortotal = 0


print("=================================================")
print("              LANCHONETE DO SENAI")
print("=================================================")

while continuar != "0":
    print("-------------------------------")
    print("          CARDÁPIO:            ")
    print("-------------------------------")
    print("1 - X-Burguer..........R$ 10,00")
    print("2 - X-Salada...........R$ 12,00")
    print("3 - Refrigerante.......R$ 5,00")
    print("4 - Batata Frita.......R$ 8,00")
    print("0 - Finalizar pedido")

    produto = (input("Digite o código do produto: "))
    print("Registrando...")
    time.sleep(1)

    match produto:
        case "0":
            continuar = "0"
        case "1":
            print("Você adicionou X-Burguer ao seu pedido.")
            valortotal += 10
            itens += 1
            print("Deseja continuar comprando? Digite 0 para encerrar o programa.")
            continuar = (input("Opção: "))
        case "2":
            print("Você adicionou X-Salada ao seu pedido.")
            valortotal += 12
            itens += 1
            print("Deseja continuar comprando?  Digite 0 para encerrar o programa.")
            continuar = (input("Opção: "))
        case "3":
            print("Você adicionou Refrigerante ao seu pedido.")
            valortotal += 5
            itens += 1
            print("Deseja continuar comprando? Digite 0 para encerrar o programa.")
            continuar = (input("Opção: "))
        case "4":
            print("Você adicionou Batata Frita ao seu pedido.")
            valortotal += 8
            itens += 1
            print("Deseja continuar comprando? Digite 0 para encerrar o programa.")
            continuar = (input("Opção: "))
        case _:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Erro:Código não listado! Tente novamente!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

if valortotal >= 20:
    desconto = True
else:
    desconto = False

print("=======================================")
print("         RESUMO DO PEDIDO            ")
print("=======================================")
print(f"Itens selecionados: {itens}")
print(f"Valor total a pagar: R${valortotal}")

if desconto == True:
    print("Desconto Aplicado!!")
    print(f"Valor com desconto: R${valortotal - valortotal*0.1:.2f}")
else:
    print("Sem descontos!!")
    print("Bom Apetite!!")