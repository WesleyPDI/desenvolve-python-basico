# Função para ler um valor inteiro com tratamento de erro
def ler_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

# Função para ler um valor em ponto flutuante com tratamento de erro
def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

# Solicita os dados dos produtos 1, 2 e 3 com tratamento de erro
nome_produto_1 = input("*Digite o nome do produto 1:* ")

preco_unitario_1 = ler_float("*Digite o preço unitário do produto 1:* ")
quantidade_1 = ler_int("*Digite a quantidade do produto 1:* ")

nome_produto_2 = input("*Digite o nome do produto 2:* ")

preco_unitario_2 = ler_float("*Digite o preço unitário do produto 2:* ")
quantidade_2 = ler_int("*Digite a quantidade do produto 2:* ")

nome_produto_3 = input("*Digite o nome do produto 3:* ")

preco_unitario_3 = ler_float("*Digite o preço unitário do produto 3:* ")
quantidade_3 = ler_int("*Digite a quantidade do produto 3:* ")

# Calcula o preço total de cada produto e o preço total da compra
preco_total_produto_1 = preco_unitario_1 * quantidade_1
preco_total_produto_2 = preco_unitario_2 * quantidade_2
preco_total_produto_3 = preco_unitario_3 * quantidade_3
preco_total_compra = preco_total_produto_1 + preco_total_produto_2 + preco_total_produto_3

# Imprime o preço total da compra formatado
print(f"Total: R${preco_total_compra:,.2f}")