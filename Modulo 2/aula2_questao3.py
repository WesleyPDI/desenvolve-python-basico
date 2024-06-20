# Inicializa as variáveis v1 e v2
v1 = 10
v2 = 20

# Exibe os valores iniciais
print(f"Antes da troca: v1 = {v1}, v2 = {v2}")

# Usa uma variável auxiliar para trocar os valores
aux = v1  # Armazena o valor de v1 em aux
v1 = v2   # Atribui o valor de v2 a v1
v2 = aux  # Atribui o valor armazenado em aux (que era v1) a v2

# Exibe os valores após a troca
print(f"Após a troca: v1 = {v1}, v2 = {v2}")