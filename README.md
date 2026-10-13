## Este é meu primeiro projeto em python, foi feito apenas para treinar meus conhecimentos, mas pode ser útil ou divertido para alguém, por isso tornei público.

# Central de Quizzes

Uma coleção de pequenos programas feitos em Python para praticar conhecimentos e facilitar tarefas do dia a dia. Os quizzes são executados pelo terminal.

## Quizzes incluídos

### 1. Quiz de Fórmula 1 (`quiz_f1.py`)
- Apresenta perguntas de múltipla escolha sobre Fórmula 1.
- Seleciona 10 perguntas aleatórias por partida, sem repetir perguntas na mesma rodada.
- Mostra o resultado ao final.

### 2. Quiz de Tabuada (`quiz_tabuada.py`)
- Faz 10 perguntas aleatórias de multiplicação.
- Usa números de 1 a 10.
- Calcula e mostra a pontuação final.

### 3. Organizador de Compras (`quiz_compras.py`)
- Pergunta o orçamento disponível.
- Ajuda a conferir produtos que estão faltando em casa, organizados por categorias.
- Usa preços aproximados para estimar os gastos.
- Monta uma lista respeitando o orçamento disponível.
- Permite adicionar produtos do catálogo ou escrever produtos personalizados.
- Permite retirar produtos e atualizar o saldo.
- Permite copiar a lista ou preparar seu compartilhamento pelo WhatsApp.
- Os preços são estimativas e devem ser conferidos no mercado.

## Arquivos do projeto

Para usar a Central de Quizzes com o menu, mantenha estes arquivos na mesma pasta:

- `menu.py` — menu principal que abre os outros programas.
- `quiz_f1.py` — quiz de Fórmula 1.
- `quiz_tabuada.py` — quiz de tabuada.
- `quiz_compras.py` — organizador de compras.

## Como executar com Python

1. Instale o Python, caso ainda não esteja instalado.
2. Coloque os arquivos `.py` na mesma pasta.
3. Abra o terminal nessa pasta.
4. Para abrir a Central de Quizzes, execute:

   python menu.py

5. Para executar apenas um programa, use, por exemplo:

   python quiz_compras.py


Os nomes dos arquivos precisam corresponder exatamente aos usados nos comandos.

## Criar um executável do Organizador de Compras

Para criar um `.exe` que possa ser executado sem instalar o Python separadamente:

1. Abra o terminal na pasta onde está `quiz_compras.py`.
2. Instale o PyInstaller:

  python -m pip install pyinstaller
 

3. Gere o executável:

 
   python -m PyInstaller --onefile --console --name "Quiz - Compras" quiz_compras.py
 

4. Quando a compilação terminar, procure o arquivo em:

   `dist/Quiz - Compras.exe`

Teste o executável antes de compartilhá-lo. O Windows pode exibir avisos de segurança para executáveis novos ou pouco conhecidos; só abra arquivos cuja origem você conhece.

## Observações

- O Organizador de Compras usa preços aproximados definidos no código, não consulta preços em tempo real.
- Ao compartilhar pelo WhatsApp, o programa prepara a mensagem, mas você ainda precisa escolher a conversa e enviá-la.
- Se alterar `quiz_compras.py`, gere novamente o `.exe` para incluir as alterações.
- Este projeto é para aprendizado e uso pessoal.
