# Lê as dimensões do terreno (comprimento e largura) e o preço por metro quadrado
comprimento = int(input("Digite o comprimento do terreno em metros: "))
largura = int(input("Digite a largura do terreno em metros: "))
preco_m2 = float(input("Digite o preço por metro quadrado em reais: "))

# Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura

# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2

# Imprime o resultado com a formatação desejada
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")