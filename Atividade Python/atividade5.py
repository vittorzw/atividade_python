def calcular_comissao(valor_produto, percentual_comissao):
    """Calcula a comissão com base no valor do produto e no percentual de comissão."""
    comissao = valor_produto * (percentual_comissao / 100)
    return comissao

# Solicitar ao usuário o valor do produto e o percentual de comissão
valor_produto = float(input("Digite o valor do produto: "))
percentual_comissao = float(input("Digite o percentual de comissão: "))

# Calcular a comissão
comissao = calcular_comissao(valor_produto, percentual_comissao)

# Exibir o resultado
print(f"A comissão para o produto de valor {valor_produto:.2f} com percentual de comissão de {percentual_comissao:.2f}% é {comissao:.2f}.")
