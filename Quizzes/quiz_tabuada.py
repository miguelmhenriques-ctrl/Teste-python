import random
import os

os.system("cls" if os.name == "nt" else "clear")

print("====================================")
print("          QUIZ DE TABUADA")
print("====================================")
print("Feito em Python por Miguel Henriques")
print("====================================")
print("      Responda as 10 perguntas!")
print()


acertos = 0
total_perguntas = 10

for i in range(1, total_perguntas + 1):
    numero1 = random.randint(1, 10)
    numero2 = random.randint(1, 10)
    resposta_correta = numero1 * numero2

    try:
        resposta = int(input(
            f"Pergunta {i}: Quanto é {numero1} x {numero2}? "
        ))

        if resposta == resposta_correta:
            print("Correto! Muito bem!")
            acertos += 1
        else:
            print(f"Errado! A resposta era {resposta_correta}.")

    except ValueError:
        print(f"Digite um número! A resposta era {resposta_correta}.")

    print()

print("==============================")
print("       RESULTADO FINAL")
print("==============================")
print(f"Acertos: {acertos} de {total_perguntas}")
print(f"Erros: {total_perguntas - acertos} de {total_perguntas}")

porcentagem = (acertos / total_perguntas) * 100
print(f"Aproveitamento: {porcentagem:.0f}%")

if acertos == 10:
    print("Perfeito! Você acertou tudo!")
elif acertos >= 7:
    print("Muito bem! Você está indo muito bem!")
elif acertos >= 5:
    print("Bom trabalho! Continue praticando!")
else:
    print("Continue treinando, você vai melhorar!")