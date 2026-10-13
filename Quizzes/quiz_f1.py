import random
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

perguntas = [
    (
        "Em que ano começou o Campeonato Mundial de F1?",
        ["1940", "1950", "1960", "1970"],
        1
    ),
    (
        "Quantas vezes Ayrton Senna foi campeão mundial?",
        ["1 vez", "2 vezes", "3 vezes", "4 vezes"],
        2
    ),
    (
        "Qual é o nome do circuito de Mônaco?",
        ["Monza", "Silverstone", "Circuit de Monaco", "Interlagos"],
        2
    ),
    (
        "O que significa conquistar a pole position?",
        [
            "Fazer a volta mais rápida da corrida",
            "Largar na primeira posição",
            "Vencer a corrida",
            "Fazer o pit stop mais rápido"
        ],
        1
    ),
    (
        "Qual bandeira indica perigo na pista?",
        ["Verde", "Amarela", "Azul", "Branca"],
        1
    ),
    (
        "Qual piloto brasileiro foi tricampeão mundial e venceu em 1981, 1983 e 1987?",
        [
            "Rubens Barrichello",
            "Felipe Massa",
            "Nelson Piquet",
            "Emerson Fittipaldi"
        ],
        2
    ),
    (
        "Para que serve o Safety Car?",
        [
            "Aumentar a velocidade dos carros",
            "Controlar o ritmo por segurança",
            "Determinar o vencedor",
            "Trocar os pneus dos pilotos"
        ],
        1
    ),
    (
        "Qual equipe é tradicionalmente conhecida pela cor vermelha?",
        ["Ferrari", "Williams", "Mercedes", "Alpine"],
        0
    ),
    (
        "O que é um pit stop?",
        [
            "Uma volta de classificação",
            "Uma parada nos boxes",
            "O início da corrida",
            "Uma penalidade"
        ],
        1
    ),
    (
        "Qual piloto conquistou seu primeiro título mundial em 2008?",
        [
            "Fernando Alonso",
            "Lewis Hamilton",
            "Sebastian Vettel",
            "Jenson Button"
        ],
        1
    ),
    (
        "O que significa a sigla DRS?",
        [
            "Driver Racing System",
            "Drag Reduction System",
            "Driving Race Speed",
            "Dynamic Road Steering"
        ],
        1
    ),
    (
        "Qual piloto conquistou seu primeiro título mundial em 2021?",
        [
            "Max Verstappen",
            "Charles Leclerc",
            "Lando Norris",
            "Kimi Raikkonen"
        ],
        0
    ),
    (
        "Qual destas pistas fica na Itália?",
        ["Silverstone", "Monza", "Suzuka", "Interlagos"],
        1
    ),
    (
        "O que a bandeira vermelha indica?",
        [
            "Fim da volta rápida",
            "Pista livre",
            "Interrupção da sessão",
            "Entrada obrigatória nos boxes"
        ],
        2
    ),
    (
        "Qual é o principal objetivo de uma corrida de F1?",
        [
            "Completar menos voltas que os outros",
            "Terminar na melhor posição possível",
            "Fazer mais pit stops",
            "Usar apenas um jogo de pneus"
        ],
        1
    )
]

perguntas_partida = random.sample(perguntas, 10)

limpar_tela()

print("=====================================")
print("           QUIZ DE FÓRMULA 1")
print("=====================================")
print("Feito em Python por Miguel Henriques")
print("=====================================")
print("    Você responderá 10 perguntas!")
print()

acertos = 0

for numero, pergunta in enumerate(perguntas_partida, start=1):
    enunciado, alternativas, correta = pergunta

    print(f"Pergunta {numero}/10:")
    print(enunciado)

    for i, alternativa in enumerate(alternativas, start=1):
        print(f"{i} - {alternativa}")

    while True:
        try:
            resposta = int(input("Sua resposta (1-4): "))

            if 1 <= resposta <= 4:
                break

            print("Digite um número de 1 a 4!")

        except ValueError:
            print("Digite apenas um número!")

    if resposta - 1 == correta:
        print("Correto!")
        acertos += 1
    else:
        print(f"Errado! Resposta correta: {alternativas[correta]}")

    print()

print("==============================")
print("       RESULTADO FINAL")
print("==============================")
print(f"Acertos: {acertos}/10")
print(f"Erros: {10 - acertos}/10")
print(f"Aproveitamento: {acertos * 10}%")

if acertos == 10:
    print("Perfeito! Você é um mestre da F1!")
elif acertos >= 7:
    print("Excelente resultado!")
elif acertos >= 5:
    print("Bom trabalho! Continue treinando!")
else:
    print("Continue estudando para a próxima corrida!")