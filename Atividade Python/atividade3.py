# Taxa de câmbio de exemplo (1 dólar para euro)
taxa_de_cambio = 0.92  # Este valor é a da cotação atual 8:19 02/08/2024

def converter_dolar_para_euro(dolares, taxa):
    return dolares * taxa

# Solicitar ao usuário a quantidade de dólares a ser convertida
dolares = float(input("Digite a quantidade de dólares que deseja converter para euros: "))

# Converter dólares para euros
euros = converter_dolar_para_euro(dolares, taxa_de_cambio)

# Exibir o resultado da conversão
print(f"{dolares} dólares equivalem a {euros:.2f} euros com a taxa de câmbio de {taxa_de_cambio}.")
