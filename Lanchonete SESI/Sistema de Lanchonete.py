import time

continuar = 1
itens = 0

print("=================================================\n")
print("              LANCHONETE DO SENAI\n")
print("=================================================")

while continuar != "0":
    print("\n-------------------------------\n")
    print("\nCARDÁPIO: ")
    print("\n1 - X-Burguer.......R$10,00")
    print("\n2 - X-Salada........R$12,00")
    print("\n3 - Refrigerante....R$5,00")
    print("\n4 - Batata Frita....R$8,00")
    print("\n0 - Finalizar o Pedido.")
    produto = input("Digite o código do produto: ")