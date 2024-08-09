def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    return sum(notas) / len(notas)

# Solicitar ao usuário que insira quatro notas
notas = []
for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)

# Calcular a média das notas
media = calcular_media(notas)

# Exibir a média das notas
print(f"A média das notas {notas} é {media:.2f}.")
