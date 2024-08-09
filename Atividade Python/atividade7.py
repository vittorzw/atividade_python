# Frase original
frase = "Ontem eu estava estudando Python."

# Buscar a posição da palavra "Python"
posicao = frase.find("Python")

# Exibir o resultado
if posicao != -1:
    print(f"A palavra 'Python' está na posição {posicao} da frase.")
else:
    print("A palavra 'Python' não foi encontrada na frase.")
