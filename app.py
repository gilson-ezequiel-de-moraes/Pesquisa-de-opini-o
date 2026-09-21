# Inicialização dos contadores
quantidade_excelente = 0
quantidade_ruim = 0

TOTAL_ENTREVISTADOS = 50

print("=========================================")
print("   PESQUISA DE SATISFAÇÃO - TUDOWEB")
print("=========================================")

# Loop para os 50 entrevistados
for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
    
    # 1. Nome (não deixa enviar em branco)
    nome = input("Digite o nome: ").strip()
    while not nome:
        print("O nome não pode ficar em branco!")
        nome = input("Digite o nome: ").strip()

    # 2. Idade (garante que é um número válido)
    idade = input("Digite a idade: ").strip()
    while not idade.isdigit() or int(idade) <= 0:
        print("Por favor, digite uma idade válida (apenas números).")
        idade = input("Digite a idade: ").strip()

    # 3. Opinião (aceita "1", "2" ou "3" sem quebrar)
    print("Opções de atendimento: [1] EXCELENTE | [2] BOM | [3] RUIM")
    opiniao = input("Digite a sua opinião (1, 2 ou 3): ").strip()
    
    while opiniao not in ["1", "2", "3"]:
        print("Opção inválida! Digite apenas 1, 2 ou 3.")
        opiniao = input("Digite a sua opinião (1, 2 ou 3): ").strip()

    # Estrutura de decisão para contabilizar os votos
    if opiniao == "1":
        quantidade_excelente += 1
    elif opiniao == "3":
        quantidade_ruim += 1

# Exibição dos resultados finais
print("\n=========================================")
print("        RESULTADO DA PESQUISA")
print("=========================================")
print(f"a) Quantidade de respostas 'EXCELENTE': {quantidade_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {quantidade_ruim}")
print("=========================================")