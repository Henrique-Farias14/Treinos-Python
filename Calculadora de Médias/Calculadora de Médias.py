continuar = "1"

while continuar != "0":
    print("--- Calculadora de Médias ---\n\n")
    aluno = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    print("Olá", aluno, "Sua Média foi de: ", media )
    if media >= 8:
        print("Você foi Aprovado")
    elif media >= 5:
        print("Você está em recuperação")
    else:
        print("Você foi reprovado")
    continuar = input("Pressione 0 para sair do programa ")
