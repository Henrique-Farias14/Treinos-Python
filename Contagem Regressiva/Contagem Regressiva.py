import time

contagem = int(input("Digite o valor da contagem: "))
while contagem != 0:
    print(f"🚀{contagem}")
    contagem -= 1
    time.sleep(1)
print("💥💥Fim da Contagem...💥💥")