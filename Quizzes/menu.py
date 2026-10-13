import subprocess
import sys
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


pasta = os.path.dirname(os.path.abspath(__file__))

while True:
    limpar_tela()

    print("========================================")
    print("           CENTRAL DE QUIZZES")
    print("========================================")
    print("Feito em Python por Miguel Henriques")
    print("========================================")
    print("1 - Quiz de Fórmula 1")
    print("2 - Quiz de tabuada")
    print("3 - Organizador de compras")
    print("0 - Sair")
    print("========================================")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        arquivo = os.path.join(pasta, "quiz_f1.py")

        if os.path.exists(arquivo):
            subprocess.run([sys.executable, arquivo])
        else:
            print("Não encontrei o arquivo quiz_f1.py!")

    elif escolha == "2":
        arquivo = os.path.join(pasta, "quiz_tabuada.py")

        if os.path.exists(arquivo):
            subprocess.run([sys.executable, arquivo])
        else:
            print("Não encontrei o arquivo quiz_tabuada.py!")

    elif escolha == "3":
        arquivo = os.path.join(pasta, "quiz_compras.py")

        if os.path.exists(arquivo):
            subprocess.run([sys.executable, arquivo])
        else:
            print("Não encontrei o arquivo quiz_compras.py!")

    elif escolha == "0":
        print("Até mais!")
        break

    else:
        print("Opção inválida!")

    input("\nPressione ENTER para voltar ao menu...")