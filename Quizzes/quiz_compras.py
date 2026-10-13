import os
import subprocess
import webbrowser
from urllib.parse import quote


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def perguntar(pergunta):
    while True:
        resposta = input(pergunta + " (S/N): ").strip().lower()

        if resposta in ["s", "sim"]:
            return True
        elif resposta in ["n", "nao", "não"]:
            return False
        else:
            print("Digite S para Sim ou N para Não.")


def perguntar_orcamento():
    while True:
        entrada = input("Quanto você pode gastar? R$ ").strip()
        entrada = entrada.replace(",", ".")

        try:
            valor = float(entrada)

            if valor > 0:
                return valor

            print("Digite um valor maior que zero.")

        except ValueError:
            print("Valor inválido. Exemplo: 150 ou 150,50.")


def perguntar_preco():
    while True:
        entrada = input("Preço estimado do produto: R$ ").strip()
        entrada = entrada.replace(",", ".")

        try:
            preco = float(entrada)

            if preco >= 0:
                return preco

            print("O preço não pode ser negativo.")

        except ValueError:
            print("Digite um preço válido. Exemplo: 12,50.")


# Preços aproximados por unidade ou embalagem.
# Altere os valores conforme os mercados da sua região.

categorias = {
    "1. ALIMENTOS BÁSICOS": [
        ("Você tem arroz suficiente?", "Arroz (5 kg)", 30.00),
        ("Você tem feijão suficiente?", "Feijão (1 kg)", 8.00),
        ("Você tem macarrão?", "Macarrão (500 g)", 4.00),
        ("Você tem óleo de cozinha?", "Óleo (900 ml)", 8.00),
        ("Você tem sal?", "Sal (1 kg)", 3.00),
        ("Você tem açúcar?", "Açúcar (1 kg)", 5.00),
        ("Você tem farinha de trigo?", "Farinha de trigo (1 kg)", 6.00),
        ("Você tem farinha de mandioca?", "Farinha de mandioca (500 g)", 6.00),
        ("Você tem fubá?", "Fubá (500 g)", 4.00),
        ("Você tem aveia?", "Aveia (pacote)", 7.00),
    ],

    "2. CARNES, OVOS E OUTRAS PROTEÍNAS": [
        ("Você tem frango?", "Frango (1 kg)", 18.00),
        ("Você tem ovos?", "Ovos (dúzia)", 12.00),
        ("Você tem carne bovina?", "Carne bovina (1 kg)", 35.00),
        ("Você tem carne suína?", "Carne suína (1 kg)", 24.00),
        ("Você tem peixe?", "Peixe (1 kg)", 25.00),
        ("Você tem linguiça?", "Linguiça (500 g)", 13.00),
        ("Você tem atum ou sardinha em lata?", "Atum ou sardinha em lata", 7.00),
        ("Você tem proteína de soja?", "Proteína de soja (pacote)", 8.00),
    ],

    "3. PÃES, CAFÉ DA MANHÃ E LATICÍNIOS": [
        ("Você tem leite?", "Leite (1 litro)", 5.00),
        ("Você tem pão?", "Pão", 10.00),
        ("Você tem café?", "Café (pacote)", 18.00),
        ("Você tem manteiga ou margarina?", "Manteiga ou margarina", 8.00),
        ("Você tem queijo?", "Queijo", 15.00),
        ("Você tem requeijão?", "Requeijão", 8.00),
        ("Você tem iogurte?", "Iogurte", 7.00),
        ("Você tem achocolatado?", "Achocolatado", 8.00),
        ("Você tem cereal matinal?", "Cereal matinal", 10.00),
        ("Você tem bolacha maisena?", "Bolacha maisena", 4.00),
        ("Você tem bolacha salgada?", "Bolacha salgada", 4.00),
    ],

    "4. TEMPEROS E MOLHOS": [
        ("Você tem alho?", "Alho", 5.00),
        ("Você tem cebola?", "Cebola", 5.00),
        ("Você tem molho de tomate?", "Molho de tomate", 3.00),
        ("Você tem vinagre?", "Vinagre", 4.00),
        ("Você tem azeite?", "Azeite", 20.00),
        ("Você tem pimenta-do-reino?", "Pimenta-do-reino", 5.00),
        ("Você tem colorau ou páprica?", "Colorau ou páprica", 5.00),
        ("Você tem orégano?", "Orégano", 4.00),
        ("Você tem caldo ou tempero pronto?", "Caldo ou tempero pronto", 4.00),
        ("Você tem maionese, ketchup ou mostarda?", "Molhos (maionese, ketchup ou mostarda)", 8.00),
    ],

    "5. FRUTAS, VERDURAS E LEGUMES": [
        ("Você tem tomate?", "Tomate", 7.00),
        ("Você tem batata?", "Batata", 6.00),
        ("Você tem cenoura?", "Cenoura", 5.00),
        ("Você tem alface?", "Alface", 4.00),
        ("Você tem couve ou outra verdura?", "Verduras", 5.00),
        ("Você tem banana?", "Banana", 6.00),
        ("Você tem maçã?", "Maçã", 8.00),
        ("Você tem laranja?", "Laranja", 6.00),
        ("Você tem limão?", "Limão", 4.00),
        ("Você tem outros legumes?", "Outros legumes", 8.00),
        ("Você tem outras frutas?", "Outras frutas", 10.00),
    ],

    "6. MERCEARIA E ENLATADOS": [
        ("Você tem milho em conserva?", "Milho em conserva", 5.00),
        ("Você tem ervilha em conserva?", "Ervilha em conserva", 5.00),
        ("Você tem seleta de legumes?", "Seleta de legumes", 6.00),
        ("Você tem creme de leite?", "Creme de leite", 4.00),
        ("Você tem leite condensado?", "Leite condensado", 7.00),
        ("Você tem gelatina?", "Gelatina", 3.00),
        ("Você tem fermento em pó?", "Fermento em pó", 4.00),
        ("Você tem pão de forma?", "Pão de forma", 9.00),
        ("Você tem tapioca?", "Tapioca (pacote)", 8.00),
        ("Você tem pipoca para panela ou micro-ondas?", "Pipoca", 4.00),
    ],

    "7. BEBIDAS": [
        ("Você tem água mineral?", "Água mineral", 3.00),
        ("Você tem suco?", "Suco", 6.00),
        ("Você tem refrigerante?", "Refrigerante", 8.00),
        ("Você tem chá?", "Chá (caixa)", 6.00),
        ("Você tem água de coco?", "Água de coco", 7.00),
    ],

    "8. LIMPEZA DA CASA": [
        ("Você tem detergente?", "Detergente", 3.00),
        ("Você tem esponja de lavar louça?", "Esponja", 3.00),
        ("Você tem desinfetante?", "Desinfetante", 7.00),
        ("Você tem água sanitária?", "Água sanitária", 5.00),
        ("Você tem limpador multiuso?", "Limpador multiuso", 7.00),
        ("Você tem limpa-vidros?", "Limpa-vidros", 8.00),
        ("Você tem panos de limpeza?", "Panos de limpeza", 8.00),
        ("Você tem sacos de lixo?", "Sacos de lixo", 8.00),
        ("Você tem luvas de limpeza?", "Luvas de limpeza", 8.00),
    ],

    "9. LAVANDERIA": [
        ("Você tem sabão para lavar roupas?", "Sabão para roupas", 12.00),
        ("Você tem amaciante?", "Amaciante", 10.00),
        ("Você tem tira-manchas?", "Tira-manchas", 12.00),
        ("Você tem pregadores de roupa?", "Pregadores de roupa", 6.00),
    ],

    "10. HIGIENE PESSOAL": [
        ("Você tem papel higiênico?", "Papel higiênico", 10.00),
        ("Você tem sabonete?", "Sabonete", 3.00),
        ("Você tem shampoo?", "Shampoo", 12.00),
        ("Você tem condicionador?", "Condicionador", 12.00),
        ("Você tem pasta de dente?", "Pasta de dente", 6.00),
        ("Você tem escova de dentes?", "Escova de dentes", 5.00),
        ("Você tem fio dental?", "Fio dental", 7.00),
        ("Você tem desodorante?", "Desodorante", 10.00),
        ("Você tem absorventes?", "Absorventes", 8.00),
        ("Você tem cotonetes?", "Cotonetes", 5.00),
    ],

    "11. PAPELARIA E ITENS DO DIA A DIA": [
        ("Você tem papel-toalha?", "Papel-toalha", 6.00),
        ("Você tem guardanapos?", "Guardanapos", 4.00),
        ("Você tem papel-alumínio?", "Papel-alumínio", 6.00),
        ("Você tem filme plástico?", "Filme plástico", 7.00),
        ("Você tem pilhas?", "Pilhas", 10.00),
        ("Você tem lâmpadas de reposição?", "Lâmpadas", 12.00),
    ],

    "12. DOCES E PETISCOS": [
        ("Você tem salgadinhos?", "Salgadinho", 4.00),
        ("Você tem bolachas recheadas?", "Bolacha recheada", 5.00),
        ("Você tem chocolate?", "Chocolate", 6.00),
        ("Você tem balas ou pirulitos?", "Balas ou pirulitos", 4.00),
        ("Você tem biscoitos doces?", "Biscoitos doces", 5.00),
        ("Você tem sorvete?", "Sorvete", 18.00),
        ("Você tem mistura para bolo?", "Mistura para bolo", 6.00),
    ],
}


def escolher_categorias(orcamento):
    # Todas as categorias são verificadas.
    # O orçamento é respeitado depois, ao montar a lista de compras.
    return list(categorias.items())


def calcular_total(lista):
    return sum(item["preco"] for item in lista)


def mostrar_lista(lista_compras, saldo):
    if not lista_compras:
        print("\nSua lista está vazia.")
    else:
        categoria_atual = None

        for numero, item in enumerate(lista_compras, start=1):
            if item["categoria"] != categoria_atual:
                categoria_atual = item["categoria"]
                print(f"\n{categoria_atual}:")

            print(
                f"  {numero}. {item['produto']} - "
                f"R$ {item['preco']:.2f}"
            )

    print("\n" + "-" * 42)
    print(f"Total estimado: R$ {calcular_total(lista_compras):.2f}")
    print(f"Saldo estimado: R$ {saldo:.2f}")


def texto_da_lista(lista_compras, orcamento):
    linhas = [
        "LISTA DE COMPRAS",
        "=" * 28,
    ]

    if not lista_compras:
        linhas.append("Nenhum produto na lista.")
    else:
        categoria_atual = None

        for item in lista_compras:
            if item["categoria"] != categoria_atual:
                categoria_atual = item["categoria"]
                linhas.append("")
                linhas.append(categoria_atual + ":")

            linhas.append(
                f"- {item['produto']} - R$ {item['preco']:.2f}"
            )

    total = calcular_total(lista_compras)

    linhas.extend([
        "",
        "-" * 28,
        f"Orçamento: R$ {orcamento:.2f}",
        f"Total estimado: R$ {total:.2f}",
        f"Saldo estimado: R$ {orcamento - total:.2f}",
        "",
        "Preços estimados; confira os valores no mercado.",
    ])

    return "\n".join(linhas)


def copiar_lista(texto):
    try:
        if os.name == "nt":
            subprocess.run(
                "clip",
                input=texto,
                text=True,
                shell=True,
                check=True,
            )
        else:
            import tkinter as tk

            janela = tk.Tk()
            janela.withdraw()
            janela.clipboard_clear()
            janela.clipboard_append(texto)
            janela.update()
            janela.destroy()

        print("\nLista copiada! Agora você pode colá-la onde quiser.")

    except Exception:
        print("\nNão consegui copiar automaticamente.")
        print("Você pode selecionar e copiar o texto abaixo:")
        print("\n" + texto)

def abrir_whatsapp(texto):
    import subprocess
    import urllib.parse

    mensagem = urllib.parse.quote(texto)
    url = "whatsapp://send?text=" + mensagem

    try:
        subprocess.run(
            ["cmd", "/c", "start", "", url],
            check=True
        )
    except Exception:
        print("Não foi possível abrir o WhatsApp.")
        print("Verifique se o aplicativo está instalado.")
        
    print("\nTentei abrir o WhatsApp Web com a lista preparada.")
    print("Escolha a conversa e envie a mensagem pelo WhatsApp.")
    print("Se pedir, entre na sua conta pelo navegador.")


# Começo do programa

limpar_tela()

print("=" * 44)
print("         ORGANIZADOR DE COMPRAS")
print("=" * 44)
print("Feito em Python por Miguel Henriques,")
print("para a praticidade na sua lista de compras")
print()
print("Informe o orçamento para começar.")
print("Os preços são estimativas, não valores em tempo real.")

orcamento = perguntar_orcamento()
saldo = orcamento

categorias_escolhidas = escolher_categorias(orcamento)

print(f"\nOrçamento: R$ {orcamento:.2f}")
print(f"Categorias que serão verificadas: {len(categorias_escolhidas)}")

input("\nPressione ENTER para começar...")

faltantes = []
total_perguntas = sum(len(itens) for _, itens in categorias_escolhidas)
contador = 0

for categoria, itens in categorias_escolhidas:
    limpar_tela()

    print("=" * 42)
    print(categoria)
    print("=" * 42)

    for pergunta, produto, preco in itens:
        contador += 1

        print(f"\nProduto {contador} de {total_perguntas}")
        print(f"Preço estimado: R$ {preco:.2f}")

        tem_produto = perguntar(pergunta)

        # Não pergunta se quer comprar.
        # Tudo o que estiver faltando vai para a seleção por orçamento.
        if not tem_produto:
            faltantes.append({
                "produto": produto,
                "preco": preco,
                "categoria": categoria,
            })


# Monta uma lista inicial respeitando a ordem de prioridade.

lista_compras = []
lista_adiante = []

for item in faltantes:
    if item["preco"] <= saldo:
        lista_compras.append(item)
        saldo -= item["preco"]
    else:
        lista_adiante.append(item)


# Catálogo para a opção de adicionar produtos na revisão.

todos_produtos = []

for categoria, itens in categorias.items():
    for pergunta, produto, preco in itens:
        todos_produtos.append({
            "produto": produto,
            "preco": preco,
            "categoria": categoria,
        })


# Revisão final: adicionar, escrever, retirar ou compartilhar.

while True:
    limpar_tela()

    print("=" * 42)
    print("       REVISAR LISTA DE COMPRAS")
    print("=" * 42)

    mostrar_lista(lista_compras, saldo)

    print("\n1 - Adicionar produto do catálogo")
    print("2 - Escrever um produto personalizado")
    print("3 - Retirar um produto")
    print("4 - Copiar a lista")
    print("5 - Abrir WhatsApp Web")
    print("0 - Terminar revisão")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "0":
        break

    elif opcao == "1":
        limpar_tela()
        print("PRODUTOS DO CATÁLOGO")
        print("=" * 42)

        for i, item in enumerate(todos_produtos, start=1):
            print(
                f"{i} - {item['produto']} "
                f"(R$ {item['preco']:.2f})"
            )

        try:
            numero = int(input("\nNúmero do produto (0 para cancelar): "))

            if numero == 0:
                continue

            if numero < 1 or numero > len(todos_produtos):
                print("Número inválido.")
            else:
                escolhido = todos_produtos[numero - 1]

                ja_adicionado = any(
                    item["produto"].casefold()
                    == escolhido["produto"].casefold()
                    for item in lista_compras
                )

                if ja_adicionado:
                    print("Esse produto já está na lista.")
                elif escolhido["preco"] > saldo:
                    print(
                        f"Não há saldo suficiente. "
                        f"Preço: R$ {escolhido['preco']:.2f}; "
                        f"saldo: R$ {saldo:.2f}."
                    )
                else:
                    lista_compras.append(escolhido)
                    saldo -= escolhido["preco"]

                    lista_adiante = [
                        item for item in lista_adiante
                        if item["produto"].casefold()
                        != escolhido["produto"].casefold()
                    ]

                    print(f"{escolhido['produto']} adicionado!")

        except ValueError:
            print("Digite um número válido.")

        input("\nPressione ENTER para continuar...")

    elif opcao == "2":
        limpar_tela()
        print("ADICIONAR PRODUTO PERSONALIZADO")
        print("=" * 42)

        nome = input("Nome do produto (ENTER para cancelar): ").strip()

        if not nome:
            continue

        ja_adicionado = any(
            item["produto"].casefold() == nome.casefold()
            for item in lista_compras
        )

        if ja_adicionado:
            print("Esse produto já está na lista.")
            input("\nPressione ENTER para continuar...")
            continue

        preco = perguntar_preco()

        if preco > saldo:
            print(
                f"\nO produto custa R$ {preco:.2f}, "
                f"mas o saldo disponível é R$ {saldo:.2f}."
            )
            print("Retire outro produto primeiro para liberar saldo.")
        else:
            lista_compras.append({
                "produto": nome,
                "preco": preco,
                "categoria": "8. PRODUTOS NÃO LISTADOS",
            })

            saldo -= preco
            print(f"\n{nome} foi adicionado à lista!")

        input("\nPressione ENTER para continuar...")

    elif opcao == "3":
        if not lista_compras:
            print("\nNão há produtos para retirar.")
            input("\nPressione ENTER para continuar...")
            continue

        print("\nQual produto deseja retirar?")

        for i, item in enumerate(lista_compras, start=1):
            print(f"{i} - {item['produto']} (R$ {item['preco']:.2f})")

        try:
            numero = int(input("\nNúmero do produto (0 para cancelar): "))

            if numero == 0:
                continue

            if numero < 1 or numero > len(lista_compras):
                print("Número inválido.")
            else:
                removido = lista_compras.pop(numero - 1)
                saldo += removido["preco"]

                print(f"\n{removido['produto']} foi retirado.")
                print(f"Saldo atualizado: R$ {saldo:.2f}")

        except ValueError:
            print("Digite um número válido.")

        input("\nPressione ENTER para continuar...")

    elif opcao == "4":
        copiar_lista(texto_da_lista(lista_compras, orcamento))
        input("\nPressione ENTER para continuar...")

    elif opcao == "5":
        abrir_whatsapp(texto_da_lista(lista_compras, orcamento))
        input("\nPressione ENTER para continuar...")

    else:
        print("Opção inválida.")
        input("\nPressione ENTER para continuar...")


# Resultado final

limpar_tela()

print("=" * 42)
print("          LISTA FINAL DE COMPRAS")
print("=" * 42)

mostrar_lista(lista_compras, saldo)

if lista_adiante:
    print("\nITENS QUE FICARAM DE FORA DO ORÇAMENTO:")

    for item in lista_adiante:
        print(f"- {item['produto']} (R$ {item['preco']:.2f})")

print("\nDeseja compartilhar a lista?")
print("1 - Copiar a lista")
print("2 - Abrir WhatsApp Web")
print("0 - Sair")

while True:
    opcao_final = input("\nEscolha uma opção: ").strip()

    if opcao_final == "1":
        copiar_lista(texto_da_lista(lista_compras, orcamento))
        break

    elif opcao_final == "2":
        abrir_whatsapp(texto_da_lista(lista_compras, orcamento))
        break

    elif opcao_final == "0":
        break

    else:
        print("Escolha 1, 2 ou 0.")

print("\nObrigado por usar o organizador de compras!")