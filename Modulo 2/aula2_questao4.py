# Inicializa as variáveis
saldo = 500.0
juros = 1.01

# Calcula o saldo após três meses de acúmulo de juros
saldo *= juros  # Saldo após o primeiro mês
saldo *= juros  # Saldo após o segundo mês
saldo *= juros  # Saldo após o terceiro mês

# Imprime o saldo final após três meses
print("Após 3 meses meu novo saldo é")
print(saldo)