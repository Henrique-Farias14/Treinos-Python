import time

alunos = [
    ["José", 8, 9],
    ["Pedro", 4, 6],
    ["Augusto", 5, 9]
]

opcao = 0

while opcao != 4:
    print("=== Cadastro de Alunos ===")
    print("1 - Cadastrar Aluno")
    print("2 - listar Alunos")
    print("3 - Consultar Média")
    print("4 - Finalizar o programa")
    try:
        opcao = int(input("Digite sua opcao: "))
        match opcao:
            case 1:
                nome = input("Digite o nome do aluno: ")
                print("Registrando...")
                time.sleep(1)
                nota1 = float(input("Digite a primeira nota: "))
                print("Registrando...")
                time.sleep(1)
                nota2 = float(input("Digite a segunda nota: "))
                print("Registrando...")
                time.sleep(1)
                print("Registrado com sucesso!")
                aluno = [nome, nota1, nota2]
                alunos.append(aluno)
            case 2:
                print("Lista de alunos cadastrados: ")
                for aluno in alunos:
                    print("Nome:", aluno[0])
                    print("Nota 1:", aluno[1])
                    print("Nota 2:", aluno[2])
                    print("----------------")
            case 3:
                print("Nome:", aluno[0])
                print("Nota 1:", aluno[1])
                print("Nota 2:", aluno[2])
                print("Média: ", aluno[1] + aluno[2] / 2)
            case 4:
                print("Finalizando o programa...")
                time.sleep(1)
            case _:
                print("Registrando...")
                time.sleep(1)
                print("Opção inválida!")
                print("Tente novamente!")
    except ValueError:
        print("Essa não é uma opção!")
        print("Tente novamente!")