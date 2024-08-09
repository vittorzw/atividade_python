# Função para coletar informações do usuário
def coletar_informacoes():
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")
    altura = input("Digite a sua altura (em metros): ")
    peso = input("Digite o seu peso (em kg): ")
    cidade = input("Digite a sua cidade: ")

    return nome, idade, altura, peso, cidade

# Função para exibir as informações do usuário
def exibir_informacoes(nome, idade, altura, peso, cidade):
    print("\n--- Informações do Usuário ---")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Altura: {altura} metros")
    print(f"Peso: {peso} kg")
    print(f"Cidade: {cidade}")

# Coletar as informações do usuário
nome, idade, altura, peso, cidade = coletar_informacoes()

# Exibir as informações do usuário
exibir_informacoes(nome, idade, altura, peso, cidade)
